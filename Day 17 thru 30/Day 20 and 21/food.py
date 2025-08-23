from turtle import Turtle,Screen
from random import randint
from snake import Snake
screen = Screen()
win_width =0

def random_position (size):
    return randint(int(-((size-50)/2)), (int(((size-50)/2))))


class Food (Turtle):
    def __init__(self, scrn):
        self.win_width = scrn.window_width()
        self.win_height = scrn.window_height()
        pos_x = random_position(self.win_width)
        pos_y = random_position(self.win_height)
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.4)
        self.color("yellow")
        self.speed("fastest")
        self.goto(x=pos_x, y=pos_y)
    def refresh(self):
        pos_x = random_position(self.win_width)
        pos_y = random_position(self.win_height)
        self.goto(x=pos_x, y=pos_y)

    def get_position(self):
        return self.position()
#
# test = Food(screen)
#
# screen.exitonclick()