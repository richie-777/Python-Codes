from turtle import Screen
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)
tim.ht()
tim.pensize(15)
directions = [0, 90, 180, 270]


def color_generator():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


for _ in range(500):
    tim.fd(30)
    tim.seth(random.choice(directions))
    tim.color(color_generator())
    tim.speed(0)

screen = Screen()
screen.exitonclick()
