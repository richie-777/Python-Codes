from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 150)
        self.write(self.l_score, align='center', font=("courier", 80, "bold"))
        self.goto(100,150)
        self.write(self.r_score, align='center', font=("courier", 80, "bold"))

    def l_point(self):
        self.clear()
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.clear()
        self.r_score += 1
        self.update_score()
