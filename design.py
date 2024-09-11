import tkinter as tk
from tkinter import colorchooser, font, filedialog
from PIL import Image, ImageTk, ImageGrab

# Create the main window
root = tk.Tk()
root.title("Advanced Interactive Event Poster Designer")
root.geometry("800x900")

# Variables for drag and drop
drag_data = {"x": 0, "y": 0, "item": None}

# Function to start drag
def on_drag_start(event):
    widget = event.widget
    drag_data["item"] = widget
    drag_data["x"] = event.x
    drag_data["y"] = event.y

# Function to handle dragging
def on_drag_motion(event):
    x = event.x - drag_data["x"]
    y = event.y - drag_data["y"]
    widget = drag_data["item"]
    widget.place(x=widget.winfo_x() + x, y=widget.winfo_y() + y)

# Function to update the text on the poster
def update_text():
    text_label.config(text=entry.get())

# Function to change font size
def change_font_size(size):
    selected_font = font.Font(size=int(size), family="Helvetica")
    text_label.config(font=selected_font)

# Function to change text color
def change_text_color():
    color = colorchooser.askcolor()[1]
    text_label.config(fg=color)

# Function to change background color of the poster
def change_bg_color():
    color = colorchooser.askcolor()[1]
    poster_frame.config(bg=color)

# Function to upload and add images
def add_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg *.jpeg *.png")])
    if file_path:
        load_image = Image.open(file_path)
        resized_image = load_image.resize((200, 200))  # Resize image for display
        poster_image = ImageTk.PhotoImage(resized_image)

        # Create a label to hold the image
        image_label = tk.Label(poster_frame, image=poster_image)
        image_label.image = poster_image  # Keep a reference to avoid garbage collection
        image_label.place(x=100, y=100)

        # Bind drag and drop functions to image
        image_label.bind("<Button-1>", on_drag_start)
        image_label.bind("<B1-Motion>", on_drag_motion)

# Function to save poster as an image
def save_poster():
    x = root.winfo_rootx() + poster_frame.winfo_x()
    y = root.winfo_rooty() + poster_frame.winfo_y()
    x1 = x + poster_frame.winfo_width()
    y1 = y + poster_frame.winfo_height()

    # Capture the poster area
    ImageGrab.grab().crop((x, y, x1, y1)).save("poster.png")
    print("Poster saved as poster.png")

# Poster frame
poster_frame = tk.Frame(root, width=600, height=700, bg='white')
poster_frame.pack(pady=20)

# Label for event text, initially empty
text_label = tk.Label(poster_frame, text="Event Title", font=("Helvetica", 40), bg="white", fg="black")
text_label.place(x=150, y=150)

# Bind drag and drop functionality to the text label
text_label.bind("<Button-1>", on_drag_start)
text_label.bind("<B1-Motion>", on_drag_motion)

# Entry for text input
entry = tk.Entry(root, font=("Helvetica", 18))
entry.pack(pady=10)

# Button to update text on poster
update_btn = tk.Button(root, text="Update Text", command=update_text)
update_btn.pack(pady=5)

# Font size slider
font_size_label = tk.Label(root, text="Select Font Size")
font_size_label.pack(pady=5)

font_size = tk.Scale(root, from_=10, to=100, orient="horizontal", command=change_font_size)
font_size.set(40)
font_size.pack(pady=5)

# Button to change text color
text_color_btn = tk.Button(root, text="Change Text Color", command=change_text_color)
text_color_btn.pack(pady=5)

# Button to change background color
bg_color_btn = tk.Button(root, text="Change Background Color", command=change_bg_color)
bg_color_btn.pack(pady=5)

# Button to upload an image to the poster
upload_image_btn = tk.Button(root, text="Add Image", command=add_image)
upload_image_btn.pack(pady=10)

# Button to save the final poster design
save_btn = tk.Button(root, text="Save Poster as Image", command=save_poster)
save_btn.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
