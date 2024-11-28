# EXIF Metadata Extractor

## Table of Contents
- [Project Description](#project-description) 
- [Authors](#authors)
- [Course Information](#course-information)
- [Installation](#installation)
- [Usage](#usage)
- [Code Overview](#code-overview)

## Project Description
The **EXIF Metadata Extractor** is a Python-based tool designed to scan directories for image files and extract their EXIF metadata. This utility provides detailed information for each image, including camera settings, timestamps, geolocation data, and more. It is an invaluable resource for photographers, forensic analysts, and anyone seeking to analyze image metadata effectively.

## Authors
This project was collaboratively developed by:
- **Christian Morrow**
- **Nyia Ware**
- **Tiara Mack**

## Course Information
- **Course:** CPSC 4100 - Survey of Programming Languages
- **Instructor:** Dr. Robert Abiodun
- **Due Date:** 30 November 2024

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
   brew install Pillow
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

The **EXIF Metadata Extractor** script is organized into three main functions for clarity and functionality:

1. **`extract_exif(file_path)`**  
   - **Purpose**: Extracts EXIF metadata from a single image file.  
   - **Parameters**:  
     - `file_path` (str): Path to the image file.  
   - **Returns**: A dictionary containing EXIF metadata.  

2. **`generate_report(metadata_list, output_file)`**  
   - **Purpose**: Generates a CSV report from the extracted metadata.  
   - **Parameters**:  
     - `metadata_list` (list): A list of dictionaries containing metadata for each image.  
     - `output_file` (str): Path to save the generated CSV file.  

3. **`main(directory, output_file)`**  
   - **Purpose**: Scans a directory for images, extracts their EXIF metadata, and optionally saves the metadata to a CSV file.  
   - **Parameters**:  
     - `directory` (str): Path to the directory containing image files.  
     - `output_file` (str, optional): Path to save the metadata report as a CSV file.  

   **Key Workflow**:  
   - Recursively searches the given directory for image files (`.jpg`, `.jpeg`, `.tiff`).  
   - Extracts EXIF metadata for each image.  
   - Outputs metadata either to the console or to a CSV file (if `--output` is specified).  
