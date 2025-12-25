from tkinter import *
from tkinter import messagebox
from math import *

# ---------------- WINDOW ----------------
root = Tk()
root.title("Scientific Calculator")
root.geometry("500x600")
root.minsize(500, 600)
root.configure(bg="#0f172a")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# ---------------- GLOBAL DATA ----------------
total_calculations = 0
error_count = 0
history_file = "History.txt"
stats_file = "Stats.txt"

# ---------------- FUNCTIONS ----------------
def press(value):
    input_entry.insert(END, value)

def clear():
    input_entry.delete(0, END)
    output_entry.config(state="normal")
    output_entry.delete(0, END)
    output_entry.config(state="readonly")

def backspace():
    if input_entry.get():
        input_entry.delete(len(input_entry.get()) - 1)

def save_history(expr, result):
    with open(history_file, "a") as f:
        f.write(f"{expr} = {result}\n")

# ---------------- SAVE STATS ----------------
def save_stats():
    with open(stats_file, "w") as f:  # create or overwrite file
        f.write(f"{total_calculations}\n")
        f.write(f"{error_count}\n")

# ---------------- CALCULATION ----------------
def calculate():
    global total_calculations, error_count
    try:
        expression = input_entry.get().replace("^", "**")
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
        output_entry.insert(0, result)
        output_entry.config(state="readonly")

        save_history(input_entry.get(), result)
        total_calculations += 1
        save_stats()  # update stats file

    except:
        error_count += 1
        output_entry.config(state="normal")
        output_entry.delete(0, END)
        output_entry.insert(0, "Error")
        output_entry.config(state="readonly")
        save_stats()  # update stats file

# ---------------- SHOW HISTORY ----------------
def show_history():
    try:
        with open(history_file, "r") as f:
            data = f.read()
        if not data:
            data = "No history found."
    except:
        data = "History file not found."
    messagebox.showinfo("History", data)

# ---------------- SHOW STATS ----------------
def show_stats():
    try:
        with open(stats_file, "r") as f:
            lines = f.readlines()
            if len(lines) >= 2:
                total = lines[0].strip()
                errors = lines[1].strip()
            else:
                total = errors = 0
    except:
        total = errors = 0
    messagebox.showinfo("Stats", f"Total Calculations: {total}\nErrors: {errors}")

def exit_app():
    save_stats()  # ensure stats are saved before exiting
    root.quit()

# ---------------- MENU ----------------
menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Clear", command=clear)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_command(label="History", command=show_history)
menu_bar.add_command(label="Stats", command=show_stats)

root.config(menu=menu_bar)

# ---------------- MAIN FRAME ----------------
main_frame = Frame(root, bg="#0f172a")
main_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

for i in range(3):
    main_frame.grid_rowconfigure(i, weight=1)
for i in range(4):
    main_frame.grid_columnconfigure(i, weight=1)

# ---------------- DISPLAY ----------------
input_entry = Entry(
    main_frame, font=("Segoe UI", 22, "bold"),
    justify="right", bg="#020617", fg="white", bd=0
)
input_entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=(0, 10))

output_entry = Entry(
    main_frame, font=("Segoe UI", 20),
    justify="right", state="readonly",
    bg="#020617", fg="#38bdf8", bd=0
)
output_entry.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=(0, 15))

# ---------------- BUTTON FRAME ----------------
btn_frame = Frame(main_frame, bg="#020617")
btn_frame.grid(row=2, column=0, columnspan=4, sticky="nsew")

for r in range(8):
    btn_frame.grid_rowconfigure(r, weight=1)
for c in range(4):
    btn_frame.grid_columnconfigure(c, weight=1)

def button(text, cmd, r, c, color):
    Button(
        btn_frame, text=text, command=cmd,
        bg=color, fg="white", bd=0,
        font=("Segoe UI", 13, "bold"),
        activebackground="#334155",
        activeforeground="white"
    ).grid(row=r, column=c, sticky="nsew", padx=5, pady=5)

# ---------------- BUTTON DATA ----------------
buttons = [
    ("C", clear), ("⌫", backspace), ("(", lambda: press("(")), (")", lambda: press(")")),
    ("7", lambda: press("7")), ("8", lambda: press("8")), ("9", lambda: press("9")), ("/", lambda: press("/")),
    ("4", lambda: press("4")), ("5", lambda: press("5")), ("6", lambda: press("6")), ("*", lambda: press("*")),
    ("1", lambda: press("1")), ("2", lambda: press("2")), ("3", lambda: press("3")), ("-", lambda: press("-")),
    ("0", lambda: press("0")), (".", lambda: press(".")), ("=", calculate), ("+", lambda: press("+")),
    ("sin", lambda: press("sin(")), ("cos", lambda: press("cos(")), ("tan", lambda: press("tan(")), ("x²", lambda: press("**2")),
    ("ln", lambda: press("ln(")), ("log", lambda: press("log(")), ("√", lambda: press("sqrt(")), ("^", lambda: press("^")),
    ("π", lambda: press("pi")), ("e", lambda: press("e")), ("//", lambda: press("//")), ("%", lambda: press("%"))
]

# ---------------- CREATE BUTTONS ----------------
row = col = 0
for text, cmd in buttons:
    if text == "C":
        color = "#ef4444"
    elif text == "=":
        color = "#22c55e"
    else:
        color = "#1e293b"

    button(text, cmd, row, col, color)

    col += 1
    if col == 4:
        col = 0
        row += 1

# ---------------- START APP ----------------
root.mainloop()
