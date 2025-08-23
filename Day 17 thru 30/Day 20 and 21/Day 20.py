#=================================== Final Challenge Snake Game ====================
#==== To solve any major problem, first break it down into sub problem
#=============== 7 Sub problems (Snake Game) Snake Day 20 and 21
#=======================Day 1 (Day 20 and 21 of challenge)
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
from food import Food
from scoreboard import Scoreboard
from turtle import Turtle, Screen
import  time
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

xy_axis = [((-(SCREEN_WIDTH -20)/2), ((SCREEN_WIDTH -20)/2)),
                 ((-(SCREEN_HEIGHT -20)/2), ((SCREEN_HEIGHT -20)/2))]

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # Turns off tracer to allow the turtle to draw smother.

snake = Snake()
food = Food(screen)
scoreboard = Scoreboard(screen)

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
    if snake.head.distance(food)< 15:
        scoreboard.score_incr()
        food.refresh()
        snake.eat_food()
    #Detect collision with wall
    if snake.head.xcor() >xy_axis[0][1] or snake.head.xcor() <xy_axis[0][0] or snake.head.ycor()>xy_axis[1][1] or snake.head.ycor() <xy_axis[1][0]:
        game_on = False
        scoreboard.game_over()

    #Detect tail collision
    for seg in snake.snakes:
        if seg != snake.head and snake.head.distance(seg) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()