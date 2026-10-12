# Day Counter for Windows

Day Counter starts at **Day 1** the first time it is opened and remembers that
date, so the count continues when the app is closed and reopened.

## Run from Python

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe .\day_counter\day_counter.py
```

## Build a standalone Windows executable

Install PyInstaller in the Python environment if it is not already installed,
then run:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller --clean --noconfirm --distpath .\day_counter\dist --workpath .\day_counter\build .\day_counter\day_counter.spec
```

The executable will be created at `day_counter\dist\DayCounter.exe`.

The start date is stored in `%APPDATA%\DayCounter\start_date.txt`.
