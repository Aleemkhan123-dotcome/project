from tkinter import *
from math import *

# ---------------- WINDOW ----------------
root = Tk()
root.title("Scientific Calculator")
root.geometry("500x650")
root.config(bg="black")
root.resizable(True, True)  # allow resizing

# ---------------- FUNCTIONS ----------------
def clear():
    input_entry.delete(0, END)
    output_entry.config(state="normal")
    output_entry.delete(0, END)
    output_entry.config(state="readonly")

def backspace():
    current = input_entry.get()
    input_entry.delete(0, END)
    input_entry.insert(0, current[:-1])

def press(value):
    input_entry.insert(END, value)

def calculation():
    try:
        expression = input_entry.get()
        expression = expression.replace("^", "**")

        result = eval(expression, {
            "__builtins__": None,
            "sin": lambda x: sin(radians(x)),
            "cos": lambda x: cos(radians(x)),
            "tan": lambda x: tan(radians(x)),
            "log": log10,
            "ln": log,
            "sqrt": sqrt,
            "pi": pi,
            "e": e
        })

        output_entry.config(state="normal")
        output_entry.delete(0, END)
        output_entry.insert(0, str(result))
        output_entry.config(state="readonly")
    except:
        output_entry.config(state="normal")
        output_entry.delete(0, END)
        output_entry.insert(0, "Error")
        output_entry.config(state="readonly")

# ---------------- MAIN FRAME ----------------
main_frame = Frame(root, bg="black")
main_frame.grid(row=0, column=0, sticky="nsew")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ---------------- ENTRIES ----------------
input_entry = Entry(main_frame, bg="#f0f0f0", borderwidth=2, relief="ridge", font="arial 20 bold", justify="right")
input_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=(10,5), ipady=10)

output_entry = Entry(main_frame, borderwidth=2, relief="ridge", font="arial 20 bold", state="readonly", bg="#e0e0e0", justify="right")
output_entry.grid(row=1, column=0, columnspan=4, sticky="nsew", padx=10, pady=(0,10), ipady=10)

# ---------------- BUTTON FRAME ----------------
btn_frame = Frame(main_frame, bg="#151573")
btn_frame.grid(row=2, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

# Make all columns in btn_frame expandable
for i in range(4):
    btn_frame.grid_columnconfigure(i, weight=1)
for i in range(8):
    btn_frame.grid_rowconfigure(i, weight=1)

def button_style(text, cmd, r, c, w=6, h=2, color="#2d2d44"):
    Button(
        btn_frame,
        text=text,
        font=("Segoe UI", 12, "bold"),
        bg=color,
        fg="white",
        bd=3,
        relief="raised",
        activebackground="#444466",
        command=cmd
    ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

# ---------------- BUTTONS ----------------
# Row 0
button_style("C", clear, 0,0, color="#ff5555")
button_style("⌫", backspace,0,1,color="#ff8844")
button_style("(", lambda: press("("),0,2)
button_style(")", lambda: press(")"),0,3)

# Row 1
button_style("1", lambda: press("1"),1,0)
button_style("2", lambda: press("2"),1,1)
button_style("3", lambda: press("3"),1,2)
button_style("4", lambda: press("4"),1,3)

# Row 2
button_style("5", lambda: press("5"),2,0)
button_style("6", lambda: press("6"),2,1)
button_style("7", lambda: press("7"),2,2)
button_style("8", lambda: press("8"),2,3)

# Row 3
button_style("9", lambda: press("9"),3,0)
button_style("0", lambda: press("0"),3,1)
button_style("=", calculation,3,2,color="#00c896")
button_style(".", lambda: press("."),3,3)

# Row 4
button_style("+", lambda: press("+"),4,0)
button_style("-", lambda: press("-"),4,1)
button_style("/", lambda: press("/"),4,2)
button_style("*", lambda: press("*"),4,3)

# Row 5 (Scientific)
button_style("sin", lambda: press("sin("),5,0)
button_style("cos", lambda: press("cos("),5,1)
button_style("tan", lambda: press("tan("),5,2)
button_style("x²", lambda: press("**2"),5,3)

# Row 6 (More scientific)
button_style("ln", lambda: press("ln("),6,0)
button_style("log", lambda: press("log("),6,1)
button_style("√", lambda: press("sqrt("),6,2)
button_style("^", lambda: press("^"),6,3)

# Row 7 (Constants)
button_style("π", lambda: press("pi"),7,0)
button_style("e", lambda: press("e"),7,1)
button_style("//", lambda: press("//"),7,2)
button_style("%", lambda: press("%"),7,3)

# Make rows in main_frame expandable
for i in range(3):
    main_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)

# ---------------- MAIN LOOP ----------------
root.mainloop()
