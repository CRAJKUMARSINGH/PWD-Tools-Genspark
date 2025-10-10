# Bridge GAD GUI Application

This is a graphical user interface version of the Bridge GAD Calculator that allows users to perform bridge engineering calculations without using the command line.

## Features

- Simple graphical interface for entering bridge parameters
- Real-time calculation of bending moment, shear force, and deflection
- Export results to Excel format
- No command-line knowledge required

## Usage

### Running the GUI Application

Double-click on `Bridge_GAD_GUI.exe` to run the application, or run it from the command line:

```
python -m bridge_gad.gui
```

### Using the Interface

1. Enter the required parameters:
   - Span (m): Length of the bridge span
   - Load (kN/m): Uniformly distributed load
   - E (kN/m²): Modulus of Elasticity (default: 2.1e8)
   - I (m⁴): Moment of Inertia (default: 0.0025)

2. Click the "Compute" button to calculate the results

3. View the results in the output area

4. Optionally, click "Export to Excel" to save the results to an Excel file

## Building the GUI Executable

If you need to rebuild the executable, run:

```
build_exe.bat
```

This will create both:
- `Bridge_GAD.exe` (CLI version)
- `Bridge_GAD_GUI.exe` (GUI version)

## Requirements

- Windows 10 or later
- No additional software required (all dependencies are included in the executable)