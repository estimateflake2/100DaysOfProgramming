# turtles.py
from turtle import Turtle

class Player(Turtle):
    def __init__(self, screen, lanes):
        super().__init__(visible=False)
        self.screen = screen
        self.lanes = lanes
        self.alive = True

        self.shape("turtle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.setheading(90)

        self._sync_with_lanes()
        self.reset_to_start()
        self.showturtle()
        self._bind_keys()

    def _sync_with_lanes(self):
        lane_h = getattr(self.lanes, "_lane_height", 40)
        self.lane_h = lane_h
        self.bottom = getattr(self.lanes, "_bottom", -self.screen.window_height()//2)
        self.top = getattr(self.lanes, "_top", self.screen.window_height()//2)
        self.left_edge = -self.screen.window_width() // 2
        self.right_edge = self.screen.window_width() // 2
        self.step_y = lane_h
        self.step_x = lane_h * 0.8
        size = (lane_h * 0.55) / 20.0
        self.shapesize(stretch_wid=size, stretch_len=size)

    def reset_to_start(self):
        self._sync_with_lanes()
        shoulder_y = self.bottom - self.lane_h * 0.5
        self.goto(0, shoulder_y)

    def _bind_keys(self):
        self.screen.listen()
        self.screen.onkeypress(self.move_up, "Up")
        self.screen.onkeypress(self.move_down, "Down")
        self.screen.onkeypress(self.move_left, "Left")
        self.screen.onkeypress(self.move_right, "Right")

    def _unbind_keys(self):
        self.screen.onkeypress(None, "Up")
        self.screen.onkeypress(None, "Down")
        self.screen.onkeypress(None, "Left")
        self.screen.onkeypress(None, "Right")

    def move_up(self):
        ny = self.ycor() + self.step_y
        if ny <= self.top:
            self.sety(ny)

    def move_down(self):
        ny = self.ycor() - self.step_y
        if ny >= self.bottom - self.lane_h * 0.5:
            self.sety(ny)

    def move_left(self):
        nx = self.xcor() - self.step_x
        if nx >= self.left_edge:
            self.setx(nx)

    def move_right(self):
        nx = self.xcor() + self.step_x
        if nx <= self.right_edge:
            self.setx(nx)

    def at_top(self):
        return self.ycor() >= self.top - self.lane_h * 0.5

    def collided(self, cars_or_list):
        cars = cars_or_list.cars if hasattr(cars_or_list, "cars") else cars_or_list
        threshold = self.lane_h * 0.6
        return any(self.distance(car) < threshold for car in cars)

    # >>> call this on game over
    def retire(self):
        self.alive = False
        self._unbind_keys()
        self.hideturtle()
        self.clear()
