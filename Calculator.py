import tkinter as tk

def click(event):
    global expression
    expression += event.widget.cget("text")
    equation.set(expression)

def evaluate(event):
    try:
        global expression
        expression = str(eval(expression))
        equation.set(expression)
    except Exception as e:
        equation.set("Error")
        expression = ""

def clear(event):
    global expression
    expression = ""
    equation.set("")

root = tk.Tk()
root.title("Simple Calculator")

# Center the calculator window on the screen
window_width = 400
window_height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))
root.geometry(f"{window_width}x{window_height}+{x_cordinate}+{y_cordinate}")

expression = ""
equation = tk.StringVar()

entry = tk.Entry(root, textvariable=equation, font=("Arial", 20), justify='right', fg="black", bg="white")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=8, pady=10)

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

for i, b in enumerate(buttons):
    button = tk.Button(root, text=b, font=("Arial", 18), height=2, width=5, bg="red", fg="white")
    button.grid(row=i//4+1, column=i%4, padx=5, pady=5)
    button.bind("<Button-1>", click if b not in ['=', 'C'] else evaluate if b == '=' else clear)

root.mainloop()
