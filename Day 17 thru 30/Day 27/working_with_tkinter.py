from tkinter import *

#=============== Day 27 - (PART 2) GUI using Tkinter & Function Arguments
#====Introduction to Tkinter
def intro_to_tkinter():
    '''introduction to tkinter using window, label and mainloop'''
    #initializing window
    window = Tk()
    window.title("My first Tkinter GUI")
    window.minsize(width =500, height=300)

    #Creating Labels:
    my_label = Label( text ='I\'m a label', font = ("Arial",24,'italic'))
    # my_label.pack(side = 'left', expand = 0) # orients the chosen object (Label) onto the window.
    # my_label.pack()
    my_label['text'] = 'New Text'

    #Creating Text
    text = Text()

    #Creating Entry Widget
    widget = Entry()

    #Creating Button
    def button_click():
        print(text.get("1.0", "end-1c"))
        print('this one is better => ', widget.get())
        my_label['text'] = 'Button Got Clicked!'
    button = Button()
    button['text'] = 'Click Me'
    button['command'] = button_click
    button.pack()
    text.pack()
    widget.pack()

    #Creating SpinBox
    spin_box = Spinbox(width=30)
    spin_box.pack()

    #List of Widgets: Label, Button, Text, Entry, Scale, SpinBox, Checkbutton, RadioButton, ListBox

    #Layout Manager
    # - Pack, Place, Grid
    #= Place: Precises location
    # difficult to manager with many componets
    # text.place (x = 100, y = 0)

    #Grid:
    # my_label.grid(column=0, row= 0)
    # text.grid(column=0, row=1)

    window.mainloop() #this code keeps the window open and listens for events/instruction. must be kept at the bottom of the code

# intro_to_tkinter()

def practice_with_grid():
    window = Tk()
    window.title("My first Tkinter GUI")
    window.minsize(width=20, height=300) ##Pads all element in the window

    # Adding Padding:
    window.config(padx=200, pady=300)

    #Creating Labels:
    my_label = Label( text ='I\'m a label 1', font = ("Arial",24,'italic'))

    my_label_2 = Label( text ='I\'m a label 2', font = ("Arial",24,'italic'))

    #Creating Text
    text = Entry()

    my_label.grid(column = 0, row = 1)
    text.grid(column = 1, row = 40)
    my_label_2.grid(column = 2, row = 0)
    window.mainloop()



practice_with_grid()


















