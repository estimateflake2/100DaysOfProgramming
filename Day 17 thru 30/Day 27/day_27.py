#=============== Day 27 - (PART 1) GUI using Tkinter & Function Arguments
#============== Final program: unit converter
import tkinter

#====Introduction to Tkinter
def intro_to_tkinter():
    '''introduction to tkinter using window, label and mainloop'''
    #initializing window
    window = tkinter.Tk()
    window.title("My first Tkinter GUI")
    window.minsize(width =500, height=300)

    #Creating Labels:
    my_label = tkinter.Label( text ='I\'m a label', font = ("Arial",24,'italic'))
    my_label.pack(side = 'left', expand = 1) # orients the chosen object (Label) onto the window.

    window.mainloop() #this code keeps the window open and listens for events/instruction. must be kept at the bottom of the code

def advanced_python_arguments():
    '''using advanced arg'''
    def my_function(a=1,b=2,c=3): #setting the values at definition sets the default value for the variable
        print('z')

def unlimited_arguments():
    '''Unlimited Positional Arguments: use *args to pass an unlimited number of arguments to a function'''
    def add(n1,n2):
        return n1+n2
    def add(*var): #use *var to collect multiple variables
        total = 0
        for n in var:
            if isinstance(n, (int, float)):
                total +=n
        return total
    print (add(1,2,3,4,"turtle",{'d': 'snake'}))

#using many key word arguments with **
def kwargs_with_multipleKeyword():
    '''using ** to generate multiple key word arguments'''
    def calculator(**kwargs):
        for (key,value) in kwargs.items():
            print ('key is: ', key, ' while value is:',value)
        print (kwargs)
    calculator (add=3, multiply= 5)

def using_kwargs():
    class Car:
        def __init__(self,**kw):
            '''note, we use get, to get the key of the dictionary rather than kw['make']. this reduces bugs if the value is not present'''
            self.make = kw.get('make')
            self.color = kw.get('color')
            self.model = kw.get('model')
    my_car = Car(make ='toyota', model='corola')
    print ('car make is: ',my_car.make)
    print ('car color is: ',my_car.color)
using_kwargs()










