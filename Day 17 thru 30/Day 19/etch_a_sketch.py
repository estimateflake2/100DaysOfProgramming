################################# Etch A Sketcha ########################
from turtle import Screen, Turtle

# Build a etch A Sketch app with the following: W=Forward, S=Backwards, A=Counter-Clockwise, D=Clockwise
tim = Turtle()
screen = Screen()

def move_foward():
    tim.forward(10)
def move_backwards():
    tim.backward(10)
def turn_c_clookwise():
    tim.left(10)
def turn_clookwise():
    tim.right(10)
def clear_reset():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key = "w", fun=move_foward)
screen.onkey(key = "s", fun=move_backwards)
screen.onkey(key = "a", fun=turn_c_clookwise)
screen.onkey(key = "d", fun=turn_clookwise)
screen.onkey(key = "c", fun=clear_reset)


screen.exitonclick()
