################################# Turtel Race App ########################
from turtle import Turtle, Screen
from random import randint
screen = Screen()

is_race_on = False
screen_width = 700
screen_height = 600
starting_x = -(screen_width/2)+20

screen.setup(width = screen_width, height=screen_height)
user_bet = screen.textinput(title="Make a Bet", prompt="Which turtle will win the race? Enter a color: ")
rbow_colors = ["red","orange","yellow","green","blue",'purple']
starting_y = [-250,-150,-50,50,150,250]
all_turtles = []

for turtles in range (0, 6):
    template_turtle = Turtle(shape="turtle")
    template_turtle.color(rbow_colors[turtles])
    template_turtle.penup()
    template_turtle.goto(x = starting_x, y= starting_y[turtles])
    all_turtles.append(template_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turte in all_turtles:
        if turte.xcor() > (screen_width/2):

            if turte.pencolor() == user_bet:
                print (f"You won! {turte.pencolor()} won")
            else:
                print(f" you lost {turte.pencolor()} won")
            is_race_on = False
            break
        rand_dist = randint(a = 0,b= 10)
        turte.forward(rand_dist)


screen.exitonclick()