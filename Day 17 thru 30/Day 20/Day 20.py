#=================================== Final Challenge Snake Game ====================
#==== To solve any major problem, first break it down into sub problem
#=============== 7 Sub problems (Snake Game) Snake Day 20
#=======================Day 1 (Day 20 of challenge)
#============== 1) Create A Snake Body
#============== 2) Move the snake
#============== 3) Control the Snake
#=======================Day 2 (Day 21 of challenge)
#============== 4) Detect collision with Food
#============== 5) Creating s Score board
#============== 6) Detect collision with wall
#============== 7) Detect collision with tail
#===================================================================================
from snake import Snake
from turtle import Turtle, Screen
import  time

screen_width = 600
screen_height = 600
screen = Screen()
screen.setup(width=screen_width, height=screen_height)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Turns off tracer to allow the turtle to draw smother.

snake = Snake()

#================Activating controll keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()


screen.exitonclick()