from turtle import Turtle

START_POS = (0,-280)
MOVE_DIST = 10
FIN_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color('black')
        self.pu()
        self.setheading(90)
        self.goto(START_POS)

    def go_up(self):
        self.fd(MOVE_DIST)

    def reset_pos(self):
        self.goto(START_POS)
