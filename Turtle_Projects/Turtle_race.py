import turtle
from turtle import Turtle, Screen
import random

screen = turtle.Screen()
screen.setup(500, 500)
user_bet = screen.textinput("make your Bet", "which turtle wins the race? Enter the color: ")
colors = ["red", 'orange', 'yellow', 'green', 'blue', 'purple']

game_on = False
y_coord = [-100, -50, 0, 50, 100, 150]
turtles = []

for turtle_index in range(0, 6):
    tim = turtle.Turtle(shape='turtle')
    tim.penup()
    tim.color(colors[turtle_index])
    tim.goto(-230, y_coord[turtle_index])
    turtles.append(tim)
# print(turtles)

if user_bet:
    game_on = True

while game_on:
    for t in turtles:
        if t.xcor() > 230:
            win_color = t.pencolor()
            if win_color == user_bet:
                print(f"You have Won! The {win_color} turtle is the winner!")
                game_on = False
            else:
                print(f"you have lost. the {win_color} turtle Won the race!")
                game_on = False
        t.fd(random.randint(1, 10))

screen.exitonclick()
