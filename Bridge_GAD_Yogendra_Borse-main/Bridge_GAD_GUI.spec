# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\bridge_gad\\gui.py'],
    pathex=[],
    binaries=[],
    datas=[('docs\\Bridge_GAD_User_Manual.md', 'docs'), ('docs\\Bridge_GAD_User_Manual.pdf', 'docs')],
    hiddenimports=['yaml', 'ezdxf', 'reportlab', 'pygame', 'numpy', 'pandas', 'matplotlib', 'openpyxl', 'scipy', 'requests', 'xlrd', 'PIL', 'tkPDFViewer'],
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
    name='Bridge_GAD_GUI',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='file_version_info.txt',
    icon=['bridge.ico'],
)
