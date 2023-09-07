from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Arial", 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.pu()
        self.goto(0, 270)
        self.ht()
        self.update_score()
    def update_score(self):
        self.write(f"score = {self.score} ", align=ALIGNMENT, font=FONT)
    def incr(self):
        self.score += 1
        self.clear()
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)
