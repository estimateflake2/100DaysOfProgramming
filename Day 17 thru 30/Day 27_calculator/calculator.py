#=============== Day 27 - (PART 3)  Tkinter Calculator App
from tkinter import *
from functools import partial

window = Tk()
window.title("Not Your Mama's Calculator")
window.iconbitmap("calculator.ico")
window.minsize(width =300, height=400)
window.config(pady=10, padx=10)

#====================Call Operational functions=====

def multiply():
    txt = display['text']
    txt_mem = display_scd['text']
    if not txt_mem or txt_mem == "Error":
        if not txt or txt == "Error":
            txt = "0"
        display_scd['text'] = f"{txt} ×"
        display['text'] = ""
        return
    if '×' in txt_mem:
        if not txt or txt == "Error":
            display['text'] = ""
            return
        try:
            res = float(txt_mem.rstrip(' ×')) * float(txt)
        except:
            display['text'] = "Error"
            display_scd['text'] = ""
            return
        if res.is_integer():
            s = str(int(res))
        else:
            s = f"{round(res, 3):.3f}".rstrip('0').rstrip('.')
            if s.startswith("0."):
                s = s[1:]
            elif s.startswith("-0."):
                s = "-" + s[2:]
        display_scd['text'] = f"{s} ×"
        display['text'] = ""
        return
    if not txt or txt == "Error":
        txt = "0"
    display_scd['text'] = f"{txt} ×"
    display['text'] = ""

def mod():
    txt = display['text']
    txt_mem = display_scd['text']
    if not txt or txt == "Error":
        txt = "0"
    else:
        if not txt_mem or txt_mem == 'Error':
            txt = '0'
            display_scd['text'] = f"{txt} %"
            display['text'] = ""
        elif '%' in txt_mem and not '0 %' in txt_mem:
            txt_mem = float(txt_mem.rstrip(' %')) % float(txt)
            display_scd['text'] = f"{txt_mem} %"
            print (f'{txt_mem} * {txt}')
            print('im here 1')
        else:
            display_scd['text'] = f"{txt} %"
            display['text'] = ""

def clear(full_reset=False):
    display ['text'] = ''
    if full_reset:
        display_scd ['text'] = ''

def delete():
    txt = display['text']
    if txt == "Error":
        display['text'] = "0"
        return
    txt = txt[:-1]
    if txt == "" or txt == "-":
        txt = "0"
    display['text'] = txt

def dot():
    txt = display['text']
    if txt == "Error":
        display['text'] = "0."
        return
    if "." not in txt:
        display['text'] = txt + "."

def frac():
    txt = display['text']
    txt_mem = display_scd['text']
    if not txt or txt == "Error":
        display['text'] = ""
        return
    try:
        val = float(txt)
    except:
        display['text'] = "Error"
        display_scd['text'] = ""
        return
    if val == 0.0:
        display['text'] = "Error"
        return
    res = 1.0 / val
    res_rounded = round(res, 3)
    s = f"{res_rounded:.3f}"
    if s.startswith("0.") and res_rounded != 0:
        s = s[1:]
    elif s.startswith("-0."):
        s = "-" + s[2:]
    display_scd['text'] = s
    display['text'] = ""

def squar():
    txt = display['text']
    if not txt or txt == "Error":
        display['text'] = ""
        return
    try:
        val = float(txt)
    except:
        display['text'] = "Error"
        display_scd['text'] = ""
        return
    res_rounded = round(val * val, 3)
    s = f"{res_rounded:.3f}"
    if s.startswith("0.") and res_rounded != 0:
        s = s[1:]
    elif s.startswith("-0."):
        s = "-" + s[2:]
    display_scd['text'] = s
    display['text'] = ""


def squart():
    txt = display['text']
    if not txt or txt == "Error":
        display['text'] = ""
        return
    try:
        val = float(txt)
    except:
        display['text'] = "Error"
        display_scd['text'] = ""
        return
    if val < 0:
        display['text'] = "Error"
        return
    res_rounded = round(val ** 0.5, 3)
    s = f"{res_rounded:.3f}"
    if s.startswith("0.") and res_rounded != 0:
        s = s[1:]
    elif s.startswith("-0."):
        s = "-" + s[2:]
    display_scd['text'] = s
    display['text'] = ""


def divide():
    txt = display['text']
    txt_mem = display_scd['text']
    if not txt_mem or txt_mem == "Error":
        if not txt or txt == "Error":
            txt = "0"
        display_scd['text'] = f"{txt} ÷"
        display['text'] = ""
        return
    if '÷' in txt_mem:
        if not txt or txt == "Error":
            display['text'] = ""
            return
        try:
            left = float(txt_mem.rstrip(' ÷'))
            right = float(txt)
            if right == 0.0:
                display['text'] = "Error"
                return
            res = left / right
        except:
            display['text'] = "Error"
            display_scd['text'] = ""
            return
        if res.is_integer():
            s = str(int(res))
        else:
            s = f"{round(res, 3):.3f}".rstrip('0').rstrip('.')
            if s.startswith("0."):
                s = s[1:]
            elif s.startswith("-0."):
                s = "-" + s[2:]
        display_scd['text'] = f"{s} ÷"
        display['text'] = ""
        return
    if not txt or txt == "Error":
        txt = "0"
    display_scd['text'] = f"{txt} ÷"
    display['text'] = ""


def subtr():
    txt = display['text']
    txt_mem = display_scd['text']
    if not txt_mem or txt_mem == "Error":
        if not txt or txt == "Error":
            txt = "0"
        display_scd['text'] = f"{txt} –"
        display['text'] = ""
        return
    if '–' in txt_mem:
        if not txt or txt == "Error":
            display['text'] = ""
            return
        try:
            left = float(txt_mem.rstrip(' –'))
            right = float(txt)
            res = left - right
        except:
            display['text'] = "Error"
            display_scd['text'] = ""
            return
        if res.is_integer():
            s = str(int(res))
        else:
            s = f"{round(res, 3):.3f}".rstrip('0').rstrip('.')
            if s.startswith("0."):
                s = s[1:]
            elif s.startswith("-0."):
                s = "-" + s[2:]
        display_scd['text'] = f"{s} –"
        display['text'] = ""
        return
    if not txt or txt == "Error":
        txt = "0"
    display_scd['text'] = f"{txt} –"
    display['text'] = ""


def addi():
    txt = display['text']
    txt_mem = display_scd['text']
    if not txt_mem or txt_mem == "Error":
        if not txt or txt == "Error":
            txt = "0"
        display_scd['text'] = f"{txt} +"
        display['text'] = ""
        return
    if '+' in txt_mem:
        if not txt or txt == "Error":
            display['text'] = ""
            return
        try:
            left = float(txt_mem.rstrip(' +'))
            right = float(txt)
            res = left + right
        except:
            display['text'] = "Error"
            display_scd['text'] = ""
            return
        if res.is_integer():
            s = str(int(res))
        else:
            s = f"{round(res, 3):.3f}".rstrip('0').rstrip('.')
            if s.startswith("0."):
                s = s[1:]
            elif s.startswith("-0."):
                s = "-" + s[2:]
        display_scd['text'] = f"{s} +"
        display['text'] = ""
        return
    if not txt or txt == "Error":
        txt = "0"
    display_scd['text'] = f"{txt} +"
    display['text'] = ""


def eql():
    txt = display['text']
    txt_mem = display_scd['text']
    if not txt_mem or txt_mem == "Error" or not txt or txt == "Error":
        display['text'] = ""
        return
    try:
        right = float(txt)
    except:
        display['text'] = "Error"
        display_scd['text'] = ""
        return
    if '×' in txt_mem:
        op = '×'
    elif '÷' in txt_mem:
        op = '÷'
    elif '–' in txt_mem:
        op = '–'
    elif '+' in txt_mem:
        op = '+'
    else:
        return
    try:
        left = float(txt_mem.rstrip(f' {op}'))
        if op == '×':
            res = left * right
        elif op == '÷':
            if right == 0.0:
                display['text'] = "Error"
                return
            res = left / right
        elif op == '–':
            res = left - right
        else:
            res = left + right
    except:
        display['text'] = "Error"
        display_scd['text'] = ""
        return
    if res.is_integer():
        s = str(int(res))
    else:
        s = f"{round(res, 3):.3f}".rstrip('0').rstrip('.')
        if s.startswith("0."):
            s = s[1:]
        elif s.startswith("-0."):
            s = "-" + s[2:]
    display_scd['text'] = s
    display['text'] = ""


def sign():
    txt = display['text']
    if txt == "Error":
        return
    if not txt:
        display['text'] = "-"
        return
    if txt == "-":
        display['text'] = ""
        return
    if txt.startswith("-"):
        display['text'] = txt[1:]
    else:
        display['text'] = "-" + txt

#opperations
ops = {'×': multiply,
       'CE': clear,
       'C':  partial(clear, full_reset=True),
       '%': mod,
       '⌫': delete,
        '1/x': frac,
        'x²': squar,
        '√x': squart,
        '÷': divide,
        '–':subtr,
        '+': addi,
        '=': eql,
        '.': dot,
        '+/-':sign,
       }

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
        _ = {k: f() for k, f in ops.items() if text == k}
        #ops.get(text)
        print(f"Pressed: {text}")


root = Frame(window)
root.pack(expand=True, fill="both")

display_scd = Label(root, anchor="e", font=("Segoe UI", 15))
display_scd.pack(fill="x", padx=6)

# Display (0 at start)
display = Label(root, text="0", anchor="e", font=("Segoe UI", 28), bg="white")
display.pack(fill="x", padx=6, pady=(6, 10))

# Memory row (6 buttons)
mem_frame = Frame(root)
mem_frame.pack(fill="x", padx=6, pady=(0, 8))

mem_buttons = ["MC", "MR", "M+", "M–", "MS", "M▾"]
for i, txt in enumerate(mem_buttons):
    b = Button(mem_frame, text=txt, state='disabled', command=lambda t=txt: on_btn(t))
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