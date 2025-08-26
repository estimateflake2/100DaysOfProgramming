#====================================== Second Capstone Project: Turtle Crossing Game
#===Objects:
    #1) ====Lanes
    #2) ====Cars
    #3) ====Turtle
    #====Level
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
BG = "black"
from turtle import Screen
from lanes import Lanes
from cars import Cars
from turtles import Player
import time
from scorecard import Scorecard


def get_lanes (difficulty = 1):
    if difficulty == 1: return 3
    elif difficulty == 1: return 5
    else: return difficulty + (difficulty%3)

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor(BG)
screen.title("Python Turtle Graphics")
screen.tracer(0)

difficulty = 1
score = Scorecard(screen, start_level=difficulty)

lanes = Lanes (screen, num_lanes=get_lanes (difficulty) )
lanes.draw()


cars = Cars(screen, lanes, count=2, base_speed=1)
player = Player(screen, lanes)

while True:
    cars.move()

    if player.collided(cars):
        difficulty =1
        # Game over: clear screen objects and restart SAME difficulty
        lanes.clear()
        cars.destroy()
        player.retire()

        score.set_level(difficulty)
        lanes = Lanes(screen, num_lanes=get_lanes(difficulty))
        lanes.draw()
        cars = Cars(screen, lanes, count=2 + difficulty*2, base_speed=1 + difficulty)
        player = Player(screen, lanes)

    elif player.at_top():
        # Level complete: increase difficulty, rebuild with more lanes/cars
        difficulty += 1
        lanes.clear()
        cars.destroy()
        player.retire()
        score.set_level(difficulty)

        lanes = Lanes(screen, num_lanes=get_lanes(difficulty))
        lanes.draw()
        cars = Cars(screen, lanes, count=2 + difficulty*2, base_speed=1 + difficulty)
        player = Player(screen, lanes)

    screen.update()
    time.sleep(0.02)


#screen.mainloop()