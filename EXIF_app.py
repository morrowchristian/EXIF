# DRAG AND DROP NEEDS WORK. ISN'T WORKING ON MY END

import os
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import TkinterDnD, DND_FILES
from PIL import Image, ExifTags
import csv


def extract_exif(file_path):
    """
    Extract EXIF metadata from an image file.
    """
    try:
        image = Image.open(file_path)
        exif_data = {
            ExifTags.TAGS.get(tag, tag): value
            for tag, value in image._getexif().items()
            if tag in ExifTags.TAGS
        }
        return exif_data
    except Exception as e:
        print(f"Error reading EXIF data from {file_path}: {e}")
        return {}


def generate_report(metadata_list, output_file):
    """
    Generate a CSV report from the extracted metadata.
    """
    try:
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=metadata_list[0].keys())
            writer.writeheader()
            writer.writerows(metadata_list)
        print(f"Metadata report saved to {output_file}")
    except Exception as e:
        print(f"Error writing report to {output_file}: {e}")


def process_file(file_path):
    """
    Process a single file and extract metadata.
    """
    if file_path.lower().endswith(('.jpg', '.jpeg', '.tiff')):
        exif_data = extract_exif(file_path)
        if exif_data:
            metadata = {"File": os.path.basename(file_path), **exif_data}
            text_box.insert(tk.END, f"Processed {file_path}\n")
            metadata_list.append(metadata)
        else:
            text_box.insert(tk.END, f"No EXIF data found in {file_path}\n")
    else:
        text_box.insert(tk.END, f"{file_path} is not a supported image file.\n")


def browse_file():
    """
    Open a file dialog to select an image file.
    """
    file_path = filedialog.askopenfilename(
        title="Select an Image File",
        filetypes=[("Image Files", "*.jpg *.jpeg *.tiff")]
    )
    if file_path:
        process_file(file_path)


def save_report():
    """
    Save the metadata report as a CSV file.
    """
    output_file = filedialog.asksaveasfilename(
        title="Save Metadata Report",
        defaultextension=".csv",
        filetypes=[("CSV Files", "*.csv")]
    )
    if output_file and metadata_list:
        generate_report(metadata_list, output_file)


def handle_drop(event):
    """
    Handle files dropped into the drag-and-drop area.
    """
    files = root.tk.splitlist(event.data)
    for file_path in files:
        process_file(file_path)


# Initialize GUI
metadata_list = []
root = TkinterDnD.Tk()
root.title("EXIF Metadata Extractor")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=20)

browse_button = tk.Button(frame, text="Browse File", command=browse_file)
browse_button.pack(side=tk.LEFT, padx=10)

save_button = tk.Button(frame, text="Save Report", command=save_report)
save_button.pack(side=tk.LEFT, padx=10)

# Drag-and-Drop Area
drop_area = tk.Label(
    root,
    text="Drag and Drop Image Files Here",
    bg="lightgray",
    relief=tk.RIDGE,
    width=50,
    height=10
)
drop_area.pack(pady=20)

# Enable drag-and-drop functionality
drop_area.drop_target_register(DND_FILES)
drop_area.dnd_bind('<<Drop>>', handle_drop)

# Text Box for Log Output
text_box = tk.Text(root, wrap=tk.WORD, height=10, width=70)
text_box.pack(pady=20)

root.mainloop()
