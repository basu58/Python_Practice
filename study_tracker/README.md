# Study Tracker

Study Tracker is a single-window desktop app for browsing the topics in
`Study_Tracker.xlsx`, filtering by area or search text, and recording completed
topics. Completion is written to each topic sheet's `Done` column using the
same check mark as the workbook, leaving the summary formulas in place.
Use **Add topic** to choose an existing area and enter the topic, subtopic,
coverage, and notes. Select a topic and choose **Delete selected** to remove it
after confirming. Both actions update the workbook and its summary formulas.
For edits to save, close the workbook in Excel and let OneDrive finish syncing
first. If Windows blocks a save, the app keeps the unsaved form contents and
explains how to retry or choose a writable workbook copy.

## Run from Python

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe .\study_tracker\study_tracker.py
```

The app opens
`%USERPROFILE%\OneDrive\Desktop\Study_Tracker.xlsx` by default. If it is not
there, choose the workbook when prompted. Use **Choose workbook...** to switch
to another tracker.

Requires `openpyxl` in the selected Python environment.

## Build a standalone Windows app

From the repository root, run:

```powershell
.\.venv\Scripts\python.exe -m PyInstaller --clean --noconfirm --distpath .\study_tracker\dist --workpath .\study_tracker\build .\study_tracker\study_tracker.spec
```

Launch `study_tracker\dist\StudyTracker.exe` by double-clicking it. The app
opens in its own window without a console.

## Tests

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s .\study_tracker -p "test_*.py"
```
