# import colorgram
#
# path = 'C:/Users/RICHIE/AppData/Local/Temp/Rar$DRa4068.25641/image.jpg'
# colors = colorgram.extract(path, 30)
# col = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     col.append((r, g, b))
# print(col)

from turtle import Turtle, Screen
import random
import turtle

new_colors = [
    (202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123),
    (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
    (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
    (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
    (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
    (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
    (176, 192, 208), (168, 99, 102)
]

tim = turtle.Turtle()
turtle.colormode(255)
tim.ht()
tim.seth(225)
tim.pu()
tim.fd(300)
tim.pd()
tim.seth(0)


def draw():
    def row():
        for _ in range(10):
            tim.speed(0)
            tim.color(random.choice(new_colors))
            tim.pd()
            tim.dot(30)
            tim.penup()
            tim.fd(50)
            tim.pendown()

    def col():
        tim.lt(90)
        tim.penup()
        tim.fd(50)
        tim.lt(90)
        tim.fd(500)
        tim.speed(0)
        tim.pendown()
        tim.lt(180)

    for _ in range(10):
        row()
        col()


draw()

screen = Screen()
screen.exitonclick()
