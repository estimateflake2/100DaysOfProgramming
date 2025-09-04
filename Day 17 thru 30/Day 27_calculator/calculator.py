#=============== Day 27 - (PART 3)  Tkinter Calculator App
from tkinter import *

window = Tk()
window.title("Calculator")
window.iconbitmap("calculator.ico")
window.minsize(width =300, height=400)
window.config(pady=10, padx=10)


#Button Press cal back
def on_btn(text):
    try:
        val = int(text)
        current = display['text']
        if current == "0":  # replace initial 0
            display['text'] = text
        else:  # append digits
            display['text'] = current + text
    except:
        print(f"Pressed: {text}")

root = Frame(window)
root.pack(expand=True, fill="both")

# Display (0 at start)
display = Label(root, text="0", anchor="e", font=("Segoe UI", 28), bg="white")
display.pack(fill="x", padx=6, pady=(6, 10))

# Memory row (6 buttons)
mem_frame = Frame(root)
mem_frame.pack(fill="x", padx=6, pady=(0, 8))

mem_buttons = ["MC", "MR", "M+", "M–", "MS", "M▾"]
for i, txt in enumerate(mem_buttons):
    b = Button(mem_frame, text=txt, command=lambda t=txt: on_btn(t))
    b.grid(row=0, column=i, padx=3, pady=3, sticky="nsew")
    mem_frame.grid_columnconfigure(i, weight=1)

keys_frame = Frame(root)
keys_frame.pack(expand=True, fill="both", padx=6, pady=(0, 6))

# Rows exactly as shown
rows = [
    ["%",  "CE", "C",   "⌫"],
    ["1/x","x²", "√x",  "÷"],
    ["7",  "8",  "9",   "×"],
    ["4",  "5",  "6",   "–"],
    ["1",  "2",  "3",   "+"],
    ["+/-","0",  ".",   "="],
]

# Configure grid weights
for r in range(len(rows) + 1):  # +1 because "=" will span into an extra row
    keys_frame.grid_rowconfigure(r, weight=1)
for c in range(4):
    keys_frame.grid_columnconfigure(c, weight=1)

# Create all buttons
for r, row in enumerate(rows):
    for c, txt in enumerate(row):
            btn = Button(keys_frame, text=txt, command=lambda t=txt: on_btn(t))
            btn.grid(row=r, column=c, padx=4, pady=4, sticky="nsew")

window.mainloop()