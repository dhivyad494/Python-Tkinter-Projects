import os
import shutil
from tkinter import *
from tkinter import filedialog, messagebox

# Function to organize files
def organize_files():
    folder_path = folder_path_var.get()
    if not folder_path:
        messagebox.showwarning("Warning", "Please select a folder first.")
        return

    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
        'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Audio': ['.mp3', '.wav', '.aac', '.ogg'],
        'Videos': ['.mp4', '.mkv', '.flv', '.avi'],
        'Archives': ['.zip', '.rar', '.tar', '.gz'],
        'Scripts': ['.py', '.js', '.html', '.css', '.php'],
        'Others': []
    }

    try:
        # Create subfolders for each file type
        for category in file_types.keys():
            category_path = os.path.join(folder_path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)

        # Move files to respective folders
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                file_extension = os.path.splitext(file_name)[1].lower()
                moved = False
                for category, extensions in file_types.items():
                    if file_extension in extensions:
                        shutil.move(file_path, os.path.join(folder_path, category, file_name))
                        moved = True
                        break
                if not moved:
                    shutil.move(file_path, os.path.join(folder_path, 'Others', file_name))

        messagebox.showinfo("Success", "Files organized successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to browse folder
def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

# GUI setup
root = Tk()
root.title("File Organizer Tool")
root.geometry("400x200")
root.config(bg="#f4f4f4")

folder_path_var = StringVar()

# Labels and buttons
Label(root, text="Select Folder to Organize:", font=("Arial", 12), bg="#f4f4f4").pack(pady=20)
Entry(root, textvariable=folder_path_var, width=40).pack(pady=10)
Button(root, text="Browse", command=browse_folder, width=10).pack(pady=5)
Button(root, text="Organize", command=organize_files, width=10, bg="#5cb85c", fg="white").pack(pady=20)

root.mainloop()
