import json, datetime, os
from os import write
from turtle import Turtle
PATH = "highscore.json"
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.path = PATH
        self.high_score = 0
        self.high_score_date = ''
        self.high_score_time = ''
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.load()
        self.update_scoreboard()

    def load (self):
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as file:
                    content = json.load(file)
                    self.high_score = int(content.get("high_score",0))
                    self.high_score_date = content.get("date", None)
                    self.high_score_time = content.get("time", None)
            except Exception:
                self.high_score = 0
                self.high_score_date = None
                self.high_score_time = None

    def save (self):
        now = datetime.datetime.now()
        data = {"high_score": self.high_score, "date": now.strftime("%Y-%m-%d"), "time": now.strftime("%H:%M:%S")}
        if self.score > self.high_score:
            data = {
                "high_score": self.score,
                "date": now.strftime("%Y-%m-%d"),
                "time": now.strftime("%H:%M:%S"),
            }
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=0)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.save()

    def reset(self):
        if self.high_score < self.score: self.high_score = self.score
        self.score = 0
        self.save()
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
