from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width =300, height=400)
window.config(pady=120, padx=150)



entry = Entry()
label = Label(text= 'Miles')
value = 0
is_equal_to_label = Label (text = f'is equal to {value} Km')

def print_to_screen(val):
    is_equal_to_label['text'] = f'is equal to {val} Km'

print_to_screen(value)

button = Button(text = 'Calculate')

#Assign Layout
entry.grid(column=2,row=1,padx=10,pady=20)

label.grid(column=3,row=1, pady=10)
is_equal_to_label.grid(column=2, row=2)
button.grid(column=2, row=3,pady=10)

def calc():
    try:
        usr_entry = int(entry.get())
        km = usr_entry * 1.60934
    except ValueError:
        km = 0
        pass

    print_to_screen(km)

button.config(command = calc)

window.mainloop()