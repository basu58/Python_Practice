# -*- mode: python ; coding: utf-8 -*-

import os

a = Analysis(
    [os.path.join(SPECPATH, "study_tracker.py")],
    pathex=[SPECPATH],
    binaries=[],
    datas=[(os.path.join(SPECPATH, "study_tracker.ico"), ".")],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    icon=os.path.join(SPECPATH, "study_tracker.ico"),
    name="StudyTracker",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
