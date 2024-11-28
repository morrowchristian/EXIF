# EXIF Metadata Extractor

## Table of Contents
- [Project Description](#project-description) 
- [Authors](#authors)
- [Course Information](#course-information)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [License](#license)

## Project Description
The EXIF Metadata Extractor is a Python-based utility that scans a given directory for image files and extracts their EXIF metadata. The program generates comprehensive details for each image, such as camera settings, timestamps, geolocation data, and more. This tool is useful for photographers, forensic analysts, and anyone who wants to gain insights into their images' metadata.

## Authors
This project was collaboratively developed by:
- Christian Morrow
- Nyia Ware
- Tiara Mack

## Course Information
- **Course:** CPSC 4100 - Survey of Programming Languages
- **Instructor:** Dr. Robert Abiodun
- **Due Date:** 30 November 2024

Here's the rewritten **Installation** and **Usage** sections of the README file, tailored for Windows, Mac, and Linux users:

---

## Installation
To use the EXIF Metadata Extractor, ensure you have Python (version 3.6 or later) installed on your system. Follow the platform-specific steps below to set up the required dependencies:

#### Windows
1. Download and install Python from [python.org](https://www.python.org/downloads/), ensuring you check the box to add Python to PATH during installation.
2. Open the Command Prompt and run the following command to install the required library:
   ```cmd
   pip install Pillow
   ```

#### Mac
1. Verify Python is installed by running `python3 --version` in the Terminal. If not, install it via [Homebrew](https://brew.sh/):
   ```bash
   brew install python
   ```
2. Install the required library:
   ```bash
   pip3 install Pillow
   ```

#### Linux
1. Use your package manager to install Python. For example, on Debian-based systems:
   ```bash
   sudo apt update
   sudo apt install python3 python3-pip
   ```
2. Install the required library:
   ```bash
   pip3 install Pillow
   ```

---

## Usage
Run the script from the command line to extract EXIF metadata from images in a specified directory. The script works on Windows, Mac, and Linux. Follow the platform-specific instructions below:

#### Windows
1. Open the Command Prompt.
2. Navigate to the directory containing the script using the `cd` command.
3. Run the script using:
   ```cmd
   python exif_extractor.py <directory> [--output <output_file>]
   ```
   Replace `<directory>` with the path to the folder containing your images, and optionally specify an output file path with `--output`.

   Example:
   ```cmd
   python exif_extractor.py C:\Users\YourName\Pictures --output metadata_report.csv
   ```

#### Mac/Linux
1. Open the Terminal.
2. Navigate to the directory containing the script using the `cd` command.
3. Run the script using:
   ```bash
   python3 exif_extractor.py <directory> [--output <output_file>]
   ```
   Replace `<directory>` with the path to the folder containing your images, and optionally specify an output file path with `--output`.

   Example:
   ```bash
   python3 exif_extractor.py /Users/YourName/Pictures --output metadata_report.csv
   ```

## Code Overview
### extract_exif(file_path)
Extracts EXIF metadata from an image file.

### generate_report(metadata_list, output_file)
Generates a CSV report from the extracted metadata.

### main(directory, output_file)
Scans a directory for images and extracts their EXIF metadata.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
