#!/usr/bin/env python3
"""
PreToolUse hook: blocks creating a new note in 01-Grammar/ or
02-Dictionary/Words/ whose name is a near-duplicate of an existing note.

This exists because of a real incident: 02-Dictionary/Words/bug.md and
bug1.md were created as separate files for the same word, and bug1.md held
real spaced-repetition review history that had to be manually recovered
during an audit. This hook makes that class of mistake impossible instead
of relying on CLAUDE.md prose being followed (Anthropic's own guidance:
hooks enforce at ~100%, prose instructions at ~70%).

Only fires on Write calls that would CREATE a new file (if the exact path
already exists, this is a normal edit and is allowed - the hook does not
interfere with editing existing notes).
"""
import json
import re
import sys
import os

WATCHED_DIRS = ("01-Grammar", "02-Dictionary/Words")


def normalize(name: str) -> str:
    """Lowercase, strip extension, strip trailing digits (bug1 -> bug)."""
    name = os.path.splitext(name)[0].lower()
    return re.sub(r"\d+$", "", name).strip()


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        # If we can't parse the input, don't block - fail open, not closed.
        sys.exit(0)

    if payload.get("tool_name") != "Write":
        sys.exit(0)

    file_path = payload.get("tool_input", {}).get("file_path", "")
    if not file_path:
        sys.exit(0)

    project_dir = os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
    abs_path = file_path if os.path.isabs(file_path) else os.path.join(project_dir, file_path)
    rel_path = os.path.relpath(abs_path, project_dir)

    if not any(rel_path.replace("\\", "/").startswith(d) for d in WATCHED_DIRS):
        sys.exit(0)

    # Editing an existing file is fine - only guard against creating a new
    # near-duplicate.
    if os.path.exists(abs_path):
        sys.exit(0)

    target_name = os.path.basename(rel_path)
    target_norm = normalize(target_name)
    target_dir = os.path.dirname(abs_path)

    if not os.path.isdir(target_dir):
        sys.exit(0)

    for existing in os.listdir(target_dir):
        if not existing.lower().endswith(".md"):
            continue
        if normalize(existing) == target_norm and normalize(existing) != "":
            print(
                json.dumps(
                    {
                        "hookSpecificOutput": {
                            "hookEventName": "PreToolUse",
                            "permissionDecision": "deny",
                            "additionalContext": (
                                f"Blocked: '{target_name}' looks like a near-duplicate of "
                                f"existing note '{existing}' in the same folder. "
                                f"This is exactly how the bug.md/bug1.md duplicate happened "
                                f"before (see ARCHITECTURE-REVIEW.md verification log) - real "
                                f"spaced-repetition review history was almost lost. "
                                f"Edit '{existing}' instead of creating a new file, or if this "
                                f"really is a different concept, rename it to something that "
                                f"doesn't collide before writing."
                            ),
                        }
                    }
                )
            )
            sys.exit(2)

    sys.exit(0)


if __name__ == "__main__":
    main()
