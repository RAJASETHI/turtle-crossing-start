from turtle import Turtle
import random as rd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_POSITION = [i for i in range(-240, 240, 5)]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.speed("slow")
        self.color(rd.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.goto(rd.randint(261, 300), rd.choice(Y_POSITION))


    def reinitialise_position(self):
        self.goto(rd.randint(261, 300), rd.choice(Y_POSITION))
        self.color(rd.choice(COLORS))