from turtle import Turtle, Screen
from player import Player
from cars import Cars
from scoreboard import Scoreboard
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
cars = Cars()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")


game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_cars()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    if player.ycor() > 275:
        scoreboard.increase_level()
        player.reset_pos()
        cars.move_speeds()

screen.exitonclick()
