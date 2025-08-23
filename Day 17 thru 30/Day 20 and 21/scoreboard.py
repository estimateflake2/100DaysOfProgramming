from turtle import Turtle, Screen
ALIGNMENT = "center"
FONT = ("Ariel", 15, "normal")

class Scoreboard (Turtle):
    def __init__(self, scrn):
        self.win_width = scrn.window_width() - 50
        self.win_height = scrn.window_height() - 50
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0,  self.win_width / 2)
        self.update_sc()
        # self.write(f"Score: {self.score}", align="center", font = ("Ariel",15,"normal"))
        self.hideturtle()
    def update_sc(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def score_incr(self):
        self.score += 1
        self.update_sc()
        # self.write(f"Score: {self.score}", align="center", font = ("Ariel",15,"normal"))
#
# screen = Screen()
# test = Scoreboard()
# screen.exitonclick()
