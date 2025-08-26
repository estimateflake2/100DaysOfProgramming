# Day 22.py
from turtle import Screen
from time import sleep

from median import Median
from levers import Lever
from ball import Ball
from scoreboard import Scoreboard

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
BG = "blue"

# screen
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG)
screen.title("My Pong Game")
screen.tracer(0)

# center dashed line
Median(screen)

# paddles
edge_x = screen.window_width() / 2
left_x = -edge_x + 40
right_x = edge_x - 40
left_paddle = Lever(left_x, screen, height=5, color="white")
right_paddle = Lever(right_x, screen, height=5, color="white")

# ball and scoreboard
ball = Ball(screen)
board = Scoreboard(screen)

# active control starts on the right
active = {"paddle": right_paddle}

def highlight():
    # visual cue for which paddle is active
    left_paddle.color("white")
    right_paddle.color("white")
    active["paddle"].color("yellow")

highlight()

def go_up():
    active["paddle"].up()

def go_down():
    active["paddle"].down()

def select_left():
    active["paddle"] = left_paddle
    highlight()

def select_right():
    active["paddle"] = right_paddle
    highlight()

screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(select_left, "Left")
screen.onkeypress(select_right, "Right")

def hit_paddle(paddle):
    within_x = abs(ball.xcor() - paddle.xcor()) < 20
    half_paddle = paddle.shapesize()[0] * 20
    within_y = paddle.ycor() - half_paddle <= ball.ycor() <= paddle.ycor() + half_paddle
    return within_x and within_y

margin_x = edge_x - 50
margin_y = screen.window_height() / 2 - 10

# game loop
while True:
    screen.update()
    sleep(ball.move_delay)
    ball.move()

    # top and bottom bounce
    if ball.ycor() > margin_y or ball.ycor() < -margin_y:
        ball.bounce_y()

    # paddle hits with automatic control transfer
    if ball.xcor() > right_paddle.xcor() - 25 and hit_paddle(right_paddle) and ball.dx > 0:
        ball.bounce_x()
        active["paddle"] = right_paddle
        highlight()

    if ball.xcor() < left_paddle.xcor() + 25 and hit_paddle(left_paddle) and ball.dx < 0:
        ball.bounce_x()
        active["paddle"] = left_paddle
        highlight()

    # scoring
    if ball.xcor() > margin_x + 40:
        board.left_point()
        ball.reset(direction="left")
        active["paddle"] = left_paddle
        highlight()

    if ball.xcor() < -margin_x - 40:
        board.right_point()
        ball.reset(direction="right")
        active["paddle"] = right_paddle
        highlight()
