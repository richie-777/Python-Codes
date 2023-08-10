import turtle
from turtle import Turtle, Screen

tim = turtle.Turtle()

screen = turtle.Screen()

tim.pensize(3)


def move_fd():
    tim.fd(50)


def move_bk():
    # tim.lt(180)
    tim.bk(50)


def move_lt():
    tim.left(20)
    # tim.fd(100)


def move_rt():
    tim.rt(20)
    # tim.fd(100)


def clear():
    tim.clear()
    tim.penup()
    tim.setpos(0, 0)
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=move_fd)
screen.onkey(key='a', fun=move_lt)
screen.onkey(key='s', fun=move_bk)
screen.onkey(key='d', fun=move_rt)
screen.onkey(key='c', fun=clear)
screen.exitonclick()
