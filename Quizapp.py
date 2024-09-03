import tkinter as tk
from tkinter import messagebox

class QuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Computer Fundamentals Quiz")
        self.master.geometry("400x300")
        
        # Questions related to Computer Fundamentals
        self.questions = [
            ("What does CPU stand for?", "Central Processing Unit", "Central Process Unit", "Computer Personal Unit", "Central Processor Unit", 1),
            ("Which of the following is an example of an input device?", "Monitor", "Keyboard", "Printer", "Speaker", 2),
            ("What is the brain of the computer?", "Memory", "Hard Drive", "CPU", "Motherboard", 3),
            ("What does RAM stand for?", "Random Access Memory", "Read Access Memory", "Run Access Memory", "Random Assignment Memory", 1),
            ("Which part of the computer is used to store data?", "RAM", "Processor", "Hard Drive", "Graphics Card", 3),
            ("What is the main function of an operating system?", "Word processing", "Managing hardware and software resources", "Data storage", "Networking", 2),
            ("Which of the following is a type of software?", "Windows", "Motherboard", "RAM", "Processor", 1),
            ("Which device is used to connect computers over a network?", "Printer", "Scanner", "Router", "Monitor", 3),
            ("What does GUI stand for?", "Graphics User Interface", "Graphical Unique Interface", "Graphical User Interface", "Graphical Universal Interface", 3),
            ("What type of memory is used for permanent data storage?", "RAM", "ROM", "Cache", "Registers", 2)
        ]
        
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(master, text=self.questions[self.current_question][0], font=("Arial", 14))
        self.question_label.pack(pady=20)
        
        self.var = tk.IntVar()
        self.var.set(-1)  # Set to an invalid value to ensure the user makes a choice
        
        self.option1 = tk.Radiobutton(master, text=self.questions[self.current_question][1], variable=self.var, value=1)
        self.option2 = tk.Radiobutton(master, text=self.questions[self.current_question][2], variable=self.var, value=2)
        self.option3 = tk.Radiobutton(master, text=self.questions[self.current_question][3], variable=self.var, value=3)
        self.option4 = tk.Radiobutton(master, text=self.questions[self.current_question][4], variable=self.var, value=4)
        
        self.option1.pack(anchor='w')
        self.option2.pack(anchor='w')
        self.option3.pack(anchor='w')
        self.option4.pack(anchor='w')
        
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_answer)
        self.submit_button.pack(pady=20)
        
    def submit_answer(self):
        selected_option = self.var.get()
        
        if selected_option == -1:
            messagebox.showwarning("No Selection", "Please select an option")
            return
        
        correct_option = self.questions[self.current_question][5]
        
        if selected_option == correct_option:
            self.score += 1
        
        self.current_question += 1
        
        if self.current_question < len(self.questions):
            self.load_next_question()
        else:
            self.show_final_score()
    
    def load_next_question(self):
        self.var.set(-1)  # Reset radio button selection
        self.question_label.config(text=self.questions[self.current_question][0])
        self.option1.config(text=self.questions[self.current_question][1])
        self.option2.config(text=self.questions[self.current_question][2])
        self.option3.config(text=self.questions[self.current_question][3])
        self.option4.config(text=self.questions[self.current_question][4])
    
    def show_final_score(self):
        messagebox.showinfo("Final Score", f"Your final score is: {self.score} out of {len(self.questions)}")
        self.master.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
