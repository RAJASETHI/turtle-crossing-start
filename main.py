import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
jimmy = Player()
screen.listen()
car = []
screen.onkeypress(jimmy.up, "Up")
game_is_on = True
sum1 = 0
total_cars = 20  # Changes with difficulty
scoreboard = Scoreboard()

move_speed = 0.01
speed = 0.1

while game_is_on:
    if len(car) < total_cars and sum1 % 4 == 0:
        for i in range(random.randint(0, 1)):
            car.append(CarManager())
    for car_name in car:
        if jimmy.distance(car_name) < 28:
            scoreboard.over()
            game_is_on = False
            break
        car_name.fd(10)
        if car_name.xcor() <= -310:
            car_name.reinitialise_position()
    if jimmy.ycor() >= 280:
        scoreboard.increment()
        jimmy.reinitialise_position()
        speed -= move_speed
    time.sleep(speed)
    screen.update()
    sum1 += 1
screen.exitonclick()
