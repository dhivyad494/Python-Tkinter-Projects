import tkinter as tk

import tkinter as tk
from tkinter import font
root = tk.Tk()
root.title("Tkinter Label")
root.geometry("400x300")
root.config(bg="#f0f0f0")
custom_font = font.Font(family="Helvetica", size=18, weight="bold")
label = tk.Label(
    root,
    text="Welcome to Tkinter!",
    font=custom_font,
    fg="white",            
    bg="blue",            
    padx=20,              
    pady=20,                 
    relief=tk.RIDGE,         
    bd=5,                    
    anchor="center",         
    cursor="hand2"           
)
def on_label_click(event):
    label.config(text="Label Clicked!", fg="#ff5733")

label.bind("<Button-1>", on_label_click)

label.pack(expand=True)

root.mainloop()
