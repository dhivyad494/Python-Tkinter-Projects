import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox

# Define file extensions categories
FILE_CATEGORIES = {
    'Images': ['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'],
    'Documents': ['pdf', 'doc', 'docx', 'txt', 'ppt', 'pptx', 'xls', 'xlsx'],
    'Videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv'],
    'Music': ['mp3', 'wav', 'aac', 'flac'],
    'Archives': ['zip', 'rar', 'tar', 'gz', '7z'],
    'Programs': ['exe', 'msi', 'bat', 'sh', 'py'],
    'Others': []
}

# Function to organize files
def organize_files():
    folder_selected = filedialog.askdirectory()  # Select folder to organize
    if folder_selected:
        organize_in_folder(folder_selected)
        messagebox.showinfo("Success", "Files organized successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a folder!")

# Function to move files to respective folders
def organize_in_folder(folder):
    for file_name in os.listdir(folder):
        file_path = os.path.join(folder, file_name)
        
        if os.path.isfile(file_path):
            # Get file extension
            file_extension = file_name.split('.')[-1].lower()

            # Determine file category
            moved = False
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    move_file(file_path, folder, category)
                    moved = True
                    break
            
            # If the file doesn't fit in any category, move to 'Others'
            if not moved:
                move_file(file_path, folder, 'Others')

# Function to move a file to a new folder
def move_file(file_path, base_folder, category):
    category_folder = os.path.join(base_folder, category)
    if not os.path.exists(category_folder):
        os.makedirs(category_folder)
    shutil.move(file_path, category_folder)

# Create the main window
root = Tk()
root.title("File Organizer")
root.geometry("400x200")

# Instructions label
label = Label(root, text="Select a folder to organize its files by file type:", font=("Arial", 12))
label.pack(pady=20)

# Button to trigger folder organization
organize_button = Button(root, text="Organize Folder", command=organize_files, font=("Arial", 12), bg="green", fg="white")
organize_button.pack(pady=10)

# Start the application
root.mainloop()
