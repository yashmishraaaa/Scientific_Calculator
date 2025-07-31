import tkinter as tk
from math import *

# Evaluate safely
def evaluate_expression(expression):
    try:
        # Replace constants
        expression = expression.replace("π", str(pi)).replace("e", str(e))
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Error"

# Button click handler
def click(button_text):
    if button_text == "=":
        result = evaluate_expression(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif button_text == "C":
        entry.delete(0, tk.END)
    elif button_text == "DEL":
        entry.delete(len(entry.get()) - 1, tk.END)
    else:
        entry.insert(tk.END, button_text)

# GUI
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, padx=10, pady=10)

buttons = [
    ["sin(", "cos(", "tan(", "log("],
    ["ln(", "√(", "^", "π"],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "(", ")"],
    ["e", "DEL", "C", "+"],
    ["=",]
]

# Create and place buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for text in row:
        btn = tk.Button(
            frame, text=text, font=("Arial", 18), relief=tk.RAISED,
            bd=5, command=lambda x=text: click(x)
        )
        btn.pack(side="left", expand=True, fill="both")

# Preprocess input for functions
def preprocess_input(expression):
    expression = expression.replace("^", "**")
    expression = expression.replace("√(", "sqrt(")
    expression = expression.replace("ln(", "log(")
    return expression

# Override evaluate_expression
def evaluate_expression(expression):
    try:
        expression = preprocess_input(expression)
        expression = expression.replace("π", str(pi)).replace("e", str(e))
        return str(eval(expression))
    except:
        return "Error"

root.mainloop()
