# scorecard.py
from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self, screen, start_level=1, padding=12, color="white",
                 font=("Arial", 18, "bold")):
        super().__init__(visible=False)
        self.screen = screen
        self.level = start_level
        self.padding = padding
        self.font = font

        self.hideturtle()
        self.penup()
        self.color(color)

        self._write_level()

    def _top_left(self):
        w = self.screen.window_width()
        h = self.screen.window_height()-50
        x = -w // 2 + self.padding
        y = h // 2 - self.padding - 2
        return x, y

    def _write_level(self):
        self.clear()
        self.goto(*self._top_left())
        self.write(f"Level: {self.level}", align="left", font=self.font)

    def set_level(self, n):
        self.level = int(n)
        self._write_level()

    def increment(self, step=1):
        self.level += step
        self._write_level()

    def destroy(self):
        self.clear()
        self.hideturtle()
