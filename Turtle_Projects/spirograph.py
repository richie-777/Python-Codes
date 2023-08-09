from turtle import Turtle, Screen
import random
import turtle

tim = turtle.Turtle()
tim.pensize(2)
turtle.colormode(255)


def color_generator():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    new_color = (r, g, b)
    return new_color


def draw_spirograph(n):
    for _ in range(int(360 / n)):
        tim.speed(0)
        tim.circle(150)
        tim.seth(tim.heading() + n)
        tim.color(color_generator())


draw_spirograph(3)

screen = Screen()
screen.exitonclick()
