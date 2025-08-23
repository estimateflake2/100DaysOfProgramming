from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Turple and array with x and y value
MOVE_PACE = 15
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class Snake:
    snakes = []

    def __init__(self):
           self.snakes = []
           self.create_snake()
           self.head = self.snakes[0]

    def create_snake (self):
        for pos in STARTING_POSITION:
            self.add_segment(pos)
    def add_segment (self, pos):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(x=pos[0], y=pos[1])
        turtle.goto(pos)  ## Same as code above
        self.snakes.append(turtle)

    def eat_food (self):
        self.add_segment(self.snakes[-1].position())

    def move(self):
        for snake_num in range(len(self.snakes) - 1, 0,
                               -1):  # moving the snake using dot position reference ( each segment of the snake moves according to the referential position of the segment infront of it.
            new_x = self.snakes[snake_num - 1].xcor()
            new_y = self.snakes[snake_num - 1].ycor()
            self.snakes[snake_num].goto(new_x, new_y)
        self.snakes[0].forward(MOVE_PACE)

    def up(self):
        if self.head.heading() != DOWN:
            self.snakes[0].setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.snakes[0].setheading(DOWN)
    def left(self):
        self.snakes[0].setheading(LEFT)
        # self.snakes[0].left(90)
    def right(self):
        self.snakes[0].setheading(RIGHT)
        # self.snakes[0].right(90)
    def get_position (self):
        return self.head.position()