from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.shapesize(1, 2)
        color = random.choice(COLORS)
        self.color(color)

    def position(self):
        self.goto(320, random.randint(-250, 250))

    def car_movement(self, speed):
        self.backward(speed)
