# lanes.py
from turtles import Turtle

class Lanes:
    def __init__(self, screen, num_lanes=3, dash_len=30, gap_len=20, top_bottom_padding=100):
        self.screen = screen
        self.num_lanes = num_lanes
        self.dash_len = dash_len
        self.gap_len = gap_len
        self.top_bottom_padding = top_bottom_padding

        self.pen = Turtle(visible=False)
        self.pen.hideturtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()

        # dims will be filled in draw()
        self._left = None
        self._right = None
        self._bottom = None
        self._top = None
        self._lane_height = None

    def draw(self):
        width = self.screen.window_width()
        height = self.screen.window_height()

        left = -width // 2
        right = width // 2
        bottom = -height // 2 + self.top_bottom_padding
        top = height // 2 - self.top_bottom_padding
        lane_height = (top - bottom) / self.num_lanes

        # save for later use
        self._left = left
        self._right = right
        self._bottom = bottom
        self._top = top
        self._lane_height = lane_height

        self.pen.clear()

        # outer boundaries
        self._draw_line(left, bottom, right, bottom)
        self._draw_line(left, top, right, top)

        # dashed separators
        for i in range(1, self.num_lanes):
            y = bottom + i * lane_height
            self._draw_dashed(left, right, y)

    def lane_center_y(self, index):
        # use cached values set by draw()
        index = max(0, min(self.num_lanes - 1, int(index)))
        return self._bottom + (index + 0.5) * self._lane_height

    def _draw_line(self, x0, y0, x1, y1):
        self.pen.penup()
        self.pen.goto(x0, y0)
        self.pen.pendown()
        self.pen.goto(x1, y1)
        self.pen.penup()

    def _draw_dashed(self, x0, x1, y):
        x = x0
        while x < x1:
            self.pen.penup()
            self.pen.goto(x, y)
            self.pen.pendown()
            self.pen.goto(min(x + self.dash_len, x1), y)
            x += self.dash_len + self.gap_len
        self.pen.penup()
    def clear(self):
        self.pen.clear()