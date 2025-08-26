#====================================== Second Capstone Project: Turtle Crossing Game
#===Objects:
    #====Cars
    #====Lanes
    #====Turtle
    #====Level
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BG = "blue"
from turtle import Screen

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG)
screen.title("Python Turtle Graphics")
screen.tracer(0)