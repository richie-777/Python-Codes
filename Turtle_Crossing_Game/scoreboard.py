from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.pu()
        self.ht()
        self.level_no = 1
        self.goto(0, 250)
        self.level()

    def level(self):
        self.clear()
        self.write(f" Level : {self.level_no}", align="center", font=FONT)

    def increase_level(self):
        self.level_no += 1
        self.level()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
