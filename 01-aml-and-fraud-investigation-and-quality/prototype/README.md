# Local Demonstration Prototype

Run from the project root:

```bash
python prototype/app.py
```

Open `http://127.0.0.1:8000`.

The app uses only Python's standard library. It loads the synthetic JSON files in `sample-data/`, calculates transaction summaries, displays pathway-specific investigative prompts and performs a checklist-based quality review.

This is a deterministic workflow prototype, not an AI/LLM system. It is intended for local demonstration only and is not hardened for production or network exposure.
