from turtle import Turtle
class Median (Turtle):
    def __init__(self, scrn):
        super().__init__()
        self.win_width = scrn.window_width() - 20
        self.win_height = scrn.window_height() - 20
        self.penup()
        self.score = 0
        self.color("white")
        self.penup()
        x = 0

        start_y = self.win_height/2
        print (start_y)
        total_length =  self.win_height
        dash = 12  # length of each dash
        gap = 8  # space between dashes
        self.goto(x, start_y)
        self.setheading(270)  # face down
        drawn = 0
        while drawn < total_length:
            # draw a dash
            self.pendown()
            step = min(dash, total_length - drawn)
            self.forward(step)
            drawn += step

            # skip the gap
            self.penup()
            if drawn < total_length:
                step = min(gap, total_length - drawn)
                self.forward(step)
                drawn += step
