#========================== Building with Turtle Graphocs, Tuples and Importing Modules



# Types of Inports
# ====================> Alias:
    #  import turtle as t
#=====================> Importing particular class
    # from turtle import Turtle

#=====================> Python package lib can be found at https://pypi.org/

#=============================== Plying with Turtle code=================
import turtle
from turtle import Turtle, Screen
t = Turtle()
s = Turtle()

s.shape("turtle")
s.color("blue")

t.shape("turtle")
t.color("chocolate4")

#===============================#===============================#========================================================

#======================Turtle Challenge 2
#=================Draw a dash line 50 times
# def dashed_line(dash_len=10, gap=6, count=50):
#     for n in range(count):
#         t.pendown()
#         t.forward(dash_len)
#         t.penup()
#         t.forward(gap)
# dashed_line()
# t.hideturtle()
#===============================#===============================#========================================================

#======================Turtle Challenge 3
# Draw a regular polygon with `sides` sides. Turn angle is the exterior angle: 360 / sides.
# Example: square -> 360 / 4 = 90, pentagon -> 360 / 5 = 72.
#========================= Tommy
# R = 120  # radius for all polygons (keeps them centered on top of each other)
# t.penup(); t.goto(0, -R); t.setheading(0); t.pendown()
#
# for sides in [3, 4, 5, 6, 7, 8, 9, 10]:  # triangle → decagon
#     t.circle(R, steps=sides)
#
# #========================= Sam
# def poly(sides, side_len):
#     turn = 360 / sides
#     for _ in range(sides):
#         s.forward(side_len)
#         s.right(turn)   # square: 360/4=90, pentagon: 360/5=72, etc.
#
# # start position
# s.penup(); s.goto(-220, 0); t.pendown()
#
# length = 240
# for n in (3, 4, 5, 6, 7, 8, 9, 10):   # triangle → decagon
#     poly(n, length)
#     length -= 18
#===============================#===============================#========================================================
#======================Turtle Challenge 3 = Random Walk
############### I couldn't quite complete this challenge. but I enjoyed learning



screen = Screen()
screen.exitonclick()