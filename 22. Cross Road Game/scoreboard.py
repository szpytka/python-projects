from turtle import Turtle

FONT = ("Comic Sans MS", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-100, 250)
        self.score(1)

    def score(self, level):
        self.clear()
        self.write(f"Level: {level}", align="right", font=FONT)

    def game_over(self):
        self.goto(0, 150)
        self.write("Game Over.", align="center", font=FONT)
