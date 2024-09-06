import tkinter as tk
from tkinter import messagebox
import json

# Function to load flashcards from a file
def load_flashcards():
    try:
        with open('flashcards.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save flashcards to a file
def save_flashcards():
    with open('flashcards.json', 'w') as file:
        json.dump(flashcards, file)

# Function to add a flashcard
def add_flashcard():
    question = entry_question.get()
    answer = entry_answer.get()
    if question and answer:
        flashcards.append({'question': question, 'answer': answer})
        save_flashcards()
        update_flashcards_list()
        entry_question.delete(0, tk.END)
        entry_answer.delete(0, tk.END)
    else:
        messagebox.showwarning('Input Error', 'Both question and answer fields are required.')

# Function to delete the selected flashcard
def delete_flashcard():
    selected_index = listbox_flashcards.curselection()
    if selected_index:
        index = selected_index[0]
        flashcards.pop(index)
        save_flashcards()
        update_flashcards_list()
    else:
        messagebox.showwarning('Selection Error', 'Please select a flashcard to delete.')

# Function to update the listbox with flashcards
def update_flashcards_list():
    listbox_flashcards.delete(0, tk.END)
    for card in flashcards:
        listbox_flashcards.insert(tk.END, card['question'])

# Function to show the answer of the selected flashcard
def show_answer():
    selected_index = listbox_flashcards.curselection()
    if selected_index:
        index = selected_index[0]
        messagebox.showinfo('Answer', flashcards[index]['answer'])
    else:
        messagebox.showwarning('Selection Error', 'Please select a flashcard to view the answer.')

# Function to quiz the user
def quiz_user():
    if not flashcards:
        messagebox.showwarning('No Flashcards', 'No flashcards available for quiz.')
        return

    correct_count = 0
    for card in flashcards:
        user_answer = tk.simpledialog.askstring('Quiz', f"Question: {card['question']}")
        if user_answer == card['answer']:
            correct_count += 1
    
    messagebox.showinfo('Quiz Result', f'You answered {correct_count} out of {len(flashcards)} questions correctly.')

# Create the main window
root = tk.Tk()
root.title('Flashcard Application')

# Load flashcards
flashcards = load_flashcards()

# Create widgets
frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text='Question:').grid(row=0, column=0, padx=5)
entry_question = tk.Entry(frame_input, width=50)
entry_question.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text='Answer:').grid(row=1, column=0, padx=5)
entry_answer = tk.Entry(frame_input, width=50)
entry_answer.grid(row=1, column=1, padx=5)

btn_add = tk.Button(frame_input, text='Add Flashcard', command=add_flashcard)
btn_add.grid(row=2, column=1, pady=10)

frame_flashcards = tk.Frame(root)
frame_flashcards.pack(pady=10)

listbox_flashcards = tk.Listbox(frame_flashcards, width=60, height=10)
listbox_flashcards.pack(side=tk.LEFT, fill=tk.BOTH)

btn_show_answer = tk.Button(frame_flashcards, text='Show Answer', command=show_answer)
btn_show_answer.pack(side=tk.TOP, pady=5)

btn_delete_flashcard = tk.Button(frame_flashcards, text='Delete Flashcard', command=delete_flashcard)
btn_delete_flashcard.pack(side=tk.TOP, pady=5)

btn_quiz = tk.Button(root, text='Start Quiz', command=quiz_user)
btn_quiz.pack(pady=10)

# Initial update of flashcards list
update_flashcards_list()

# Start the main event loop
root.mainloop()
