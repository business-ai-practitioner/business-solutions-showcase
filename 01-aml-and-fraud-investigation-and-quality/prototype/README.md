# Local prototype

## Requirements

- Python 3.9 or later.
- No third-party Python packages.

## Run

From the root of this project:

```bash
python prototype/app.py
```

Open `http://127.0.0.1:8000`.

Stop the server with `Ctrl+C`.

## What it does

- Reads the three JSON examples in `sample-data/`.
- Calculates transaction totals from the supplied records.
- Displays the case-specific pathway prompts and evidence gaps.
- Applies simple completeness checks to the supplied case fields.
- Shows a small management-theme summary across the sample cases.
- Provides a JSON export for the selected case.

## Technical design

The app uses Python's built-in `http.server`, `json`, `html`, `urllib` and `pathlib` modules. It is intentionally simple so the workflow can be inspected without installing packages.

The checks are transparent rules, not AI. They are not calibrated, validated or suitable for operational decisions. The server binds to `127.0.0.1` so it is available only on the local computer by default.

## Known limitations

- Fixed sample data; no case entry or document upload.
- No authentication or role-based access.
- No database or audit log.
- No external service or AI model.
- No production security or resilience controls.
- Checklist flags are prompts only and require human assessment.
