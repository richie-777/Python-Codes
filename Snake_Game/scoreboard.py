from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.ht()
        self.update_score()

    def update_score(self):
        self.write(f"score : {self.score}   High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()

    def incr(self):
        self.score += 1
        self.clear()
        self.update_score()
