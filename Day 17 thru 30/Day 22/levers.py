# levers.py
from turtle import Turtle

class Lever(Turtle):
    def __init__(self, x, screen, height=5, color="white", step=30):
        super().__init__(visible=False)
        self.screen = screen
        self.step = step
        self.color(color)
        self.shape("square")
        # tall paddle: height rows, 1 column
        self.shapesize(stretch_wid=height, stretch_len=1)
        self.penup()
        self.goto(x, 0)
        self.showturtle()

    def _limit(self, y):
        half_h = self.screen.window_height() / 2
        # small padding so it does not clip outside the window
        pad = 10
        # paddle draws from center, so subtract half its height in pixels (height*20)
        half_paddle = self.shapesize()[0] * 20
        top_limit = half_h - pad - half_paddle
        bot_limit = -half_h + pad + half_paddle
        return max(min(y, top_limit), bot_limit)

    def up(self):
        y = self.ycor() + self.step
        self.sety(self._limit(y))

    def down(self):
        y = self.ycor() - self.step
        self.sety(self._limit(y))
