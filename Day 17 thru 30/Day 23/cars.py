# cars.py
from turtles import Turtle
import random

class Car(Turtle):
    COLORS = ["red", "blue", "green", "yellow", "purple", "orange", "cyan", "magenta"]

    def __init__(self, screen, lanes, speed=5):
        super().__init__(visible=False)
        self.screen = screen
        self.lanes = lanes
        self.speed_px = speed

        # setup turtle
        self.shape("square")
        self.color(random.choice(self.COLORS))
        self.penup()

        # size the car relative to lane height
        lane_h = getattr(self.lanes, "_lane_height", None)
        if lane_h is None:
            height = self.screen.window_height()
            bottom_pad = getattr(self.lanes, "top_bottom_padding", 0)
            lane_h = (height - 2 * bottom_pad) / self.lanes.num_lanes

        self.shapesize(stretch_wid=(lane_h * 0.6) / 20.0, stretch_len=2.2)

        self.reset_position()
        self.showturtle()

    def reset_position(self):
        width = self.screen.window_width()
        start_x = width // 2 + 40   # always start from right edge
        lane_index = random.randint(0, self.lanes.num_lanes - 1)
        y = self.lanes.lane_center_y(lane_index)
        self.goto(start_x, y)
        self.color(random.choice(self.COLORS))

    def move(self):
        self.setx(self.xcor() - self.speed_px)
        if self.xcor() < -self.screen.window_width() // 2 - 60:
            self.reset_position()

    def set_speed(self, speed):
        self.speed_px = max(0, speed)


class Cars:
    def __init__(self, screen, lanes, count=10, base_speed=5):
        self.cars = [Car(screen, lanes, speed=base_speed + random.randint(0, 3))
                     for _ in range(count)]

    def move(self):
        for c in self.cars:
            c.move()

    def set_speed(self, speed):
        for c in self.cars:
            c.set_speed(speed)
    def destroy(self):
        for c in self.cars:
            c.hideturtle()
            c.clear()
        self.cars.clear()