# EXIF Metadata Extractor  

## Project Description  
The **EXIF Metadata Extractor** is a Python-based utility that scans a given directory for image files and extracts their EXIF metadata. The program generates comprehensive details for each image, such as camera settings, timestamps, geolocation data, and more. This tool is useful for photographers, forensic analysts, and anyone who wants to gain insights into their images' metadata.

---

## Table of Contents  
- [Project Description](#project-description)  
- [Features](#features)  
- [Installation](#installation)  
- [Usage](#usage)  
- [Authors](#authors)  
- [Course Information](#course-information)  

---

## Features  
- Extract EXIF metadata from all image files in a specified directory.  
- Support for popular image formats, including JPEG and TIFF.  
- Display comprehensive details such as:  
  - Camera make and model.  
  - Date and time the photo was taken.  
  - GPS coordinates (if available).  
  - Image dimensions and resolution.  
- Generate a detailed report in human-readable or CSV format.  

---

## Installation  

### Prerequisites  
- Python 3.9 or higher.  
- `Pillow` library for image processing.  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/ChristianMorrow/EXIF_Metadata_Extractor.git  
   cd EXIF_Metadata_Extractor  
   ```  
2. Install dependencies:  
   ```bash  
   pip install -r requirements.txt  
   ```  

---

## Usage  

1. Run the script with the target directory as an argument:  
   ```bash  
   python exif_extractor.py /path/to/images  
   ```  

2. Output options:  
   - Metadata details printed to the console.  
   - Optional report saved in CSV format:  
     ```bash  
     python exif_extractor.py /path/to/images --output report.csv  
     ```  

3. View or analyze the generated CSV using any spreadsheet tool for further insights.  

---

## Authors  
This project was collaboratively developed by:  
- **Christian Morrow**  
- **Nyia Ware**  
- **Tiara Mack**  

---

## Course Information  
- **Course**: CPSC 4100 - Survey of Programming Languages  
- **Instructor**: Dr. Robert Abiodun  
- **Due Date**: 30 November 2024  

---

## Contributions  
We welcome contributions to this project! Please fork the repository, make your changes, and submit a pull request for review.  

--- 

Feel free to customize this `README.md` further to fit any additional needs!
