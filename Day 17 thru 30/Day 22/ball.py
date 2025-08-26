# ball.py
from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, screen, speed_px=6):
        super().__init__(visible=False)
        self.screen = screen
        self.color("orange")
        self.shape("circle")
        self.penup()
        self.move_px = speed_px           # base pixel speed per frame
        self.dx = speed_px
        self.dy = random.choice([-4, -3, 3, 4])
        self.move_delay = 0.015           # controls time.sleep in the loop
        self.reset(direction=random.choice(["left", "right"]))
        self.showturtle()

    def reset(self, direction="right"):
        self.goto(0, 0)
        self.move_delay = 0.015
        self.dy = random.choice([-4, -3, 3, 4])
        self.dx = abs(self.move_px) if direction == "right" else -abs(self.move_px)

    def move(self):
        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def bounce_y(self):
        self.dy *= -1

    def bounce_x(self):
        self.dx *= -1
        # slight acceleration after paddle hit
        self.move_delay = max(0.006, self.move_delay * 0.92)
