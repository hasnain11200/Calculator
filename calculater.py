import tkinter as tk

# Window setup
root = tk.Tk()
root.title("VIP Calculator")
root.geometry("400x550")
root.configure(bg="#2C3E50")
root.resizable(0,0)

# Entry box
entry = tk.Entry(root, font=("Arial", 15, "bold"), bd=5, relief="sunken", justify="right", bg="#ECF0F1")
entry.pack(fill="both", ipadx=8, pady=20, padx=10)

# Functions
def button_click(item):
    entry.insert(tk.END, item)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except: 
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout
button_frame = tk.Frame(root, bg="#2C3E50")
button_frame.pack()

buttons = [
           ['7', '8', '9', '/'],
           ['4', '5', '6', '*'],
           ['1', '2', '3', '-'],
           ['0', '.', '=', '+'],
           [        'C'        ],
   ]

# Styling buttons
for r, row in enumerate(buttons):
    for c, char in enumerate(row):
        if char == '=':
            tk.Button(button_frame, text=char, width=8, height=3, bg="#27AE60", fg="white", font=("Arial", 10, "bold"), command=calculate).grid(row=r, column=c, padx=5, pady=5)
        elif char == 'C':
            tk.Button(button_frame, text=char, width=8, height=3, bg="#E74C3C", fg="white", font=("Arial", 10, "bold"), command=clear).grid(row=r, column=0, columnspan=4, padx=5, pady=5)
        else:
            tk.Button(button_frame, text=char, width=8, height=3, bg="#34495E", fg="white", font=("Arial", 10, "bold"), command=lambda ch=char: button_click(ch)).grid(row=r, column=c, padx=5, pady=5)

root.mainloop()