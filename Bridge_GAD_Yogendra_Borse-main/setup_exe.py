from cx_Freeze import setup, Executable
import sys

# Dependencies are automatically detected, but it might need fine tuning.
build_options = {
    'packages': ['bridge_gad', 'numpy', 'pandas', 'matplotlib', 'openpyxl', 'scipy'],
    'excludes': [],
    'include_files': []
}

base = 'Win32GUI' if sys.platform == 'win32' else None

executables = [
    Executable('bridge_gad_exe.py', base=base, target_name='Bridge_GAD.exe')
]

setup(
    name='Bridge_GAD',
    version='0.1',
    description='Bridge General Arrangement Drawing Generator',
    options={'build_exe': build_options},
    executables=executables
)