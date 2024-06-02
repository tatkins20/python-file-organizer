"""
File Organizer with GUI

This script organizes files in a specified directory into folders based on their file extensions.
The user can input the directory, file extensions, and corresponding folder names through a GUI.

Dependencies:
    - Python 3.x
    - shutil module (for moving files)
    - tkinter module (for GUI)

Usage:
    1. Run the script.
    2. Input the directory, file extensions, and corresponding folder names in the GUI.
    3. Click the 'Organize Files' button.

Example:
    If you have files like 'example.jpg', 'report.pdf', and 'music.mp3' in your specified directory,
    after running the script and inputting the details through the GUI, these files will be organized
    into respective folders:
    - Images: example.jpg
    - Docs: report.pdf
    - Audio: music.mp3
"""

import os
import shutil
import tkinter as tk
from tkinter import filedialog

def organize_files():
    directory = directory_entry.get()
    extensions_text = extensions_entry.get("1.0", tk.END)

    # Parse extensions and corresponding folder names
    extensions = {}
    for line in extensions_text.split("\n"):
        if line.strip():
            ext, folder = line.strip().split(":")
            extensions[ext.strip()] = folder.strip()

    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Check if it's a file
        if os.path.isfile(file_path):
            # Get the file extension
            extension = os.path.splitext(filename)[1].lower()

            # If the extension is defined in the extensions dictionary
            if extension in extensions:
                folder_name = extensions[extension]

                # Create folder if it doesn't exist
                folder_path = os.path.join(directory, folder_name)
                os.makedirs(folder_path, exist_ok=True)

                # Move the file to its corresponding folder
                destination_path = os.path.join(folder_path, filename)
                shutil.move(file_path, destination_path)

                print(f"Moved {filename} to {folder_name} folder.")
            else:
                # If extension is not defined, skip the file
                print(f"Skipped {filename}. Unknown file extension.")
        else:
            # Skip directories
            print(f"Skipped {filename}. It is a directory.")

    # Print completion message
    print("File organization completed!")

# Create GUI window
root = tk.Tk()
root.title("File Organizer")

# Directory input
directory_label = tk.Label(root, text="Directory:")
directory_label.grid(row=0, column=0, sticky="w")
directory_entry = tk.Entry(root)
directory_entry.grid(row=0, column=1, padx=5, pady=5)
directory_button = tk.Button(root, text="Browse", command=lambda: directory_entry.insert(tk.END, filedialog.askdirectory()))
directory_button.grid(row=0, column=2, padx=5, pady=5)

# Extensions input
extensions_label = tk.Label(root, text="Extensions and Folder Names (e.g., .jpg: Images):")
extensions_label.grid(row=1, column=0, sticky="w")
extensions_entry = tk.Text(root, height=5, width=40)
extensions_entry.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

# Organize button
organize_button = tk.Button(root, text="Organize Files", command=organize_files)
organize_button.grid(row=2, column=1, pady=10)

root.mainloop()
