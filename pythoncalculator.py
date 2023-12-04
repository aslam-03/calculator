import tkinter as tk

def on_button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear_entry():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")


# Entry widget to display input and results
entry = tk.Entry(root, width=20, font=('Arial', 16), bd=5, insertwidth=4, justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Define button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Create and place buttons with custom colors
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, width=5, height=2, font=('Arial', 16),
                       bg='black', fg='white',  # Setting background and foreground colors
                       command=lambda t=text: on_button_click(t) if t not in {'=', 'C'} else calculate() if t == '=' else clear_entry())
    button.grid(row=row, column=col)


# Run the main loop
root.mainloop()

