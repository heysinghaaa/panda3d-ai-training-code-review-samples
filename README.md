# panda3d-ai-training-code-review-samples

Code review samples for Python/Panda3D-style game logic, written in an AI training and evaluation format.

The repository contains intentionally small examples that focus on practical review skills: identifying runtime bugs, frame-rate issues, input handling mistakes, asset-path assumptions, collision/proximity edge cases, and maintainability problems.

## What This Demonstrates

- Python code review for interactive 3D/game-development snippets
- Panda3D concepts such as task loops, scene updates, loader usage, and camera/input flow
- Clear bug reports with expected behavior, observed behavior, root cause, and suggested fixes
- AI-training style feedback that is concise, grounded, and actionable
- Small pure-Python helper tests for the review reasoning

## Repository Layout

```text
.
├── samples/
│   ├── task_loop/
│   ├── input_handling/
│   ├── proximity_logic/
│   └── asset_loading/
├── reviews/
├── src/panda3d_review_helpers/
├── tests/
└── templates/
```

## How To Run The Tests

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```

The tests do not require a Panda3D window. They validate the pure-Python helper logic used in the review examples.

## Review Format

Each review uses a consistent structure:

- Summary
- Severity
- Observed issue
- Why it matters
- Suggested fix
- Edge cases to test

This mirrors the kind of clear written evaluation expected in AI code-review and model-training tasks.

