# scoreboard.py
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, screen, color="white"):
        super().__init__(visible=False)
        self.screen = screen
        self.color(color)
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_text()

    def update_text(self):
        self.clear()
        w = self.screen.window_width()
        y = self.screen.window_height() / 2 - 60
        # Left score
        self.goto(-w/4, y)
        self.write(f"{self.l_score}", align="center", font=("Courier", 36, "bold"))
        # Right score
        self.goto(w/4, y)
        self.write(f"{self.r_score}", align="center", font=("Courier", 36, "bold"))

    def left_point(self):
        self.l_score += 1
        self.update_text()

    def right_point(self):
        self.r_score += 1
        self.update_text()
