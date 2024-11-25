# EXIF Metadata Extractor

## Table of Contents
- Project Description
- Authors
- Course Information
- Installation
- Usage
- Example
- Code Overview
  - extract_exif(file_path)
  - generate_report(metadata_list, output_file)
  - main(directory, output_file)
- License

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

## Installation
To use the EXIF Metadata Extractor, you need to have Python installed on your system along with the required libraries. You can install the necessary libraries using pip:

```bash
pip install Pillow
```

## Usage
To run the EXIF Metadata Extractor, use the following command:

```bash
python exif_extractor.py <directory> [--output <output_file>]
```

- `<directory>`: Path to the directory containing image files.
- `--output <output_file>`: Optional path to save the metadata report as a CSV file.

## Example
```bash
python exif_extractor.py /path/to/images --output metadata_report.csv
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
