# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\bridge_gad\\cli.py'],
    pathex=[],
    binaries=[],
    datas=[('src\\bridge_gad\\*.py', 'bridge_gad')],
    hiddenimports=['yaml', 'ezdxf', 'reportlab', 'pygame', 'numpy', 'pandas', 'matplotlib', 'openpyxl', 'scipy', 'requests', 'xlrd', 'PIL'],
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
    name='Bridge_GAD',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
