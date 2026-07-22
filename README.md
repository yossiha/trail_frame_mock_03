# Relay Finance — Python/Flask fixture

A small server-rendered expense-claim flow. It intentionally avoids a JavaScript framework so TrailFrame can exercise a non-Node application.

## Run

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

## Run with TrailFrame

```powershell
node .\apps\cli\dist\bin.js run --contract ..\trail_frame_mock_03\journey-contract.json --project ..\trail_frame_mock_03 --start "python app.py" --ready-url "http://127.0.0.1:4183/"
```

The baseline permits submission without an optional project code. The fixture PR incorrectly makes that optional field required.
