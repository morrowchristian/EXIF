# EXIF Metadata Extractor

## Description
The **EXIF Metadata Extractor** is a Python-based tool designed to analyze directories for image files and extract their EXIF metadata. It provides detailed information about each image, including camera settings, timestamps, geolocation data, and more. This utility is invaluable for photographers, forensic analysts, and anyone seeking to analyze image metadata effectively.

---

## Features
- **EXIF Metadata Extraction**: Extract key details from image files like `JPG`, `JPEG`, and `TIFF`.
- **CSV Report Generation**: Save extracted metadata as a CSV file for further analysis.
- **Drag-and-Drop Functionality**: Easily add image files by dragging and dropping them into the application.
- **Cross-Platform GUI**: A user-friendly interface built using Tkinter and TkinterDnD.

---

## Authors
- Christian Morrow  
- Nyia Ware  
- Tiara Mack  

**Course**: CPSC 4100 - Survey of Programming Languages  
**Instructor**: Dr. Robert Abiodun  
**Due Date**: November 30, 2024  

---

## Installation

### Prerequisites
1. **Python**: Ensure Python 3.8 or later is installed.
2. **PIP**: Ensure you have Python's package manager installed.

### Install Required Libraries
Run the following command to install the dependencies:
```bash
pip install pillow tkinterdnd2
```

If you encounter issues:
- **Pillow Installation**: Refer to the [Pillow documentation](https://pillow.readthedocs.io/en/stable/installation.html) for troubleshooting.
- **TkinterDnD2 Installation**: Check the [TkinterDnD2 GitHub page](https://github.com/pearu/tkinterdnd2) for guidance.

---

## Setup Instructions

### Windows
1. Clone the repository:
   ```bash
   git clone https://github.com/morrowchristian/EXIF.git
   cd EXIF
   ```
2. Run the application:
   ```bash
   python EXIF_app.py
   ```
3. If TkinterDnD2 installation fails, see [this guide](https://github.com/pearu/tkinterdnd2#installation).

### macOS
1. Install Python dependencies as above.
2. If drag-and-drop functionality doesn't work, grant permissions in **System Preferences** → **Security & Privacy** → **Accessibility**.
3. Run the application:
   ```bash
   python EXIF_app.py
   ```
4. For macOS-specific Tkinter issues, check the [Apple Developer Community](https://developer.apple.com/forums/) for help.

### Linux
1. Install required libraries:
   ```bash
   sudo apt install python3-tk python3-pil
   pip install tkinterdnd2
   ```
2. Run the application:
   ```bash
   python3 EXIF_app.py
   ```
3. Refer to [Tkinter Troubleshooting on Linux](https://wiki.python.org/moin/TkInter) for help with installation issues.

---

## Usage

1. **Launch the Application**: Run the script with `python exif_extractor.py`.
2. **Add Files**: Use the "Browse File" button or drag-and-drop image files into the labeled area.
3. **Process Files**: The application will display logs for each processed file in the text box.
4. **Save Reports**: Click the "Save Report" button to export metadata to a CSV file.

---

## Code Overview

### Main Components
1. **`extract_exif`**: Extracts EXIF metadata from image files using the PIL library.
2. **`generate_report`**: Saves metadata into a CSV file.
3. **GUI**: Built using Tkinter, includes buttons for browsing files, saving reports, and drag-and-drop functionality.

### Known Issue
- **Drag-and-Drop**: May not work on some macOS systems due to OS-level restrictions. Run the application with elevated permissions or refer to [TkinterDnD2 issues](https://github.com/pearu/tkinterdnd2/issues).

---

## Examples

### Extract Metadata
1. Drag a `.jpg` file into the drag-and-drop area.
2. Check the log for details like:
   ```
   Processed example.jpg
   ```

### Save a Report
1. Click "Save Report".
2. Specify the output file location:
   ```
   C:\Users\<User>\Documents\metadata_report.csv
   ```

---

## Troubleshooting

1. **Python Installation Issues**:
   - **Windows**: Use [Python's Windows installation guide](https://docs.python.org/3/using/windows.html).
   - **macOS**: Refer to [Python on macOS](https://docs.python.org/3/using/mac.html).
   - **Linux**: Follow [Linux installation instructions](https://docs.python.org/3/using/unix.html).

2. **Pillow Issues**:
   - Refer to the [Pillow troubleshooting guide](https://pillow.readthedocs.io/en/stable/installation.html#troubleshooting).

3. **Tkinter Issues**:
   - [General Tkinter Installation Help](https://tkdocs.com/tutorial/install.html).

4. **TkinterDnD2 Errors**:
   - Review [TkinterDnD2 issues](https://github.com/pearu/tkinterdnd2/issues) on GitHub.

5. **Drag-and-Drop Not Working**:
   - macOS: Check [System Preferences for Accessibility Permissions](https://support.apple.com/en-us/HT201899).
   - Windows/Linux: Verify file path handling by adding debug logs in the `handle_drop` function.

---

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contributions
If you encounter issues or have suggestions, please submit a pull request or file an issue in this repository.  
