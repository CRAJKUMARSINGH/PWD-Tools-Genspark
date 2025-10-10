# Bridge GAD Executable

This folder contains the executable version of the Bridge GAD Generator.

## Usage

### Running the Executable

Double-click on `Bridge_GAD.exe` to run the application, or run it from the command line:

```
Bridge_GAD.exe --span 20 --load 15
```

### Command Line Options

- `--span`: Span length of beam (m)
- `--load`: Uniformly distributed load (kN/m)
- `--E`: Modulus of Elasticity (kN/m²) [default: 2.1e8]
- `--I`: Moment of Inertia (m⁴) [default: 0.0025]
- `--output`: Optional path to save Excel results

### Example

```
Bridge_GAD.exe --span 20 --load 15 --E 2.1e8 --I 0.0025 --output results.xlsx
```

## Building the Executable

If you need to rebuild the executable, run:

```
build_exe.bat
```

This requires PyInstaller to be installed:

```
pip install pyinstaller
```

## Requirements

- Windows 10 or later
- No additional software required (all dependencies are included in the executable)