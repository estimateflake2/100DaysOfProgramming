#========================== Day 19 1) Turtle Graphics, 2) Event Listeners, 3) State and Multiple Instances
from turtle import Turtle, Screen
#============================================================2)  Event Listeners
tim = Turtle()
tim.shape("turtle")
tom = Turtle()
tom.shape("turtle")
screen = Screen()
#
# def move_foward():
#     tim.forward(10)
#
# screen.listen()
#
# #================= Note: when passing a function to another function (ie: onkey (move_forward()), we only pass the name of the function
# screen.onkey(key = "space", fun=move_foward)  # When using borrowed libs, use keyword arguments to call your function instead
# screen.exitonclick()
#==== Build an etch_a_sketch app (see etch_a_sketch.py)================


#============================================================3)  Event State
# Set is the condition of each variable in a given instance of an object
tim.color("green")
tom.color("red")
tom.forward(10)
#==== Build an turtle racing app (see turtle_race.py)================

screen.exitonclick()