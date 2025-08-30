MAP_IMAGE = "resource/day-25-us-states-game-start/blank_states_img.gif"
STATES_CSV = "resource/day-25-us-states-game-start/50_states.csv"
from collections.abc import Mapping
from turtle import Screen, Turtle
import pandas

#=============pandas data
content = pandas.read_csv(STATES_CSV)

turtle = Turtle()
turtle.hideturtle()
screen = Screen()
screen.title("US States Game")
screen.setup(width=725, height=491)  # match your GIF size if you know it
# image = "resource/day-25-us-states-game-start/blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
screen.bgpic(MAP_IMAGE)  # GIF works reliably with turtle


def write_state(state_name, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.write(state_name)
    turtle.penup()



data_found = []
inp_title = "Guess the State"
score = 0
while score <50:
    ans = screen.textinput(title=inp_title, prompt="What is the name of a state?")
    ans_location = content[content.state.str.strip().str.lower() == ans.strip().lower()]
    if len(ans_location) > 0 and not data_found.__contains__(ans_location['state'].iloc[0]):
        data_found.append(ans_location['state'].iloc[0])
        write_state(ans_location['state'].iloc[0], ans_location['x'].iloc[0], ans_location['y'].iloc[0])
        score += 1
        inp_title = str(score) + "/ 50"
    else:
        pass




# def get_mouse_click_coor (x,y):
#     print(x,y)
# screen.onscreenclick(get_mouse_click_coor)
screen.mainloop()
