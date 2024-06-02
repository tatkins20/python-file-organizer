# python-file-organizer
# File Organizer with GUI

This Python script helps you organize files in a specified directory into folders based on their file extensions. The user can input the directory, file extensions, and corresponding folder names through a graphical user interface (GUI) built using Tkinter.

## Features

- **Easy to Use:** Simply run the script, input the directory and file organization details via the GUI, and click the 'Organize Files' button.
- **Customizable:** Define your own file extensions and corresponding folder names to suit your needs.
- **Efficient:** Organize your files quickly and efficiently without the hassle of manually moving them around.

## Dependencies

- Python 3.x
- shutil module (for moving files)
- tkinter module (for GUI)

## Usage

1. **Run the Script:** Execute the script in your Python environment.
2. **Input Details:** Use the GUI to specify the directory and define extensions with their corresponding folder names.
3. **Organize Files:** Click the 'Organize Files' button to start the file organization process.

## Example

Suppose you have files like 'example.jpg', 'report.pdf', and 'music.mp3' in your specified directory. After running the script and inputting the details through the GUI, these files will be organized into respective folders:

- **Images:** example.jpg
- **Docs:** report.pdf
- **Audio:** music.mp3

## How to Run

1. Clone this repository to your local machine.
2. Ensure you have Python 3.x installed.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Run the script using `python file_organizer_gui.py`.
5. Follow the instructions on the GUI to organize your files.
