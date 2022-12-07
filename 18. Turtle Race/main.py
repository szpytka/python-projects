import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.",
                            prompt="Which turtle will win the race? Enter a color: (red/orange/black/green/blue/purple)")
colors = ["red", "orange", "black", "green", "blue", "purple"]
turtles = ["turtle1", "turtle2", "turtle3", "turtle4", "turtle5", "turtle6"]
starting_x = -230
starting_y = -170

for i in range(6):
    turtles[i] = Turtle("turtle")
    turtles[i].turtlesize(2)
    turtles[i].color(colors[i])
    turtles[i].penup()
    starting_y += 50
    turtles[i].goto(x=starting_x, y=starting_y)

if user_bet:
    is_race_on = True

while is_race_on:
    for i in range(6):
        if turtles[i].xcor() > 200:
            is_race_on = False
            winning_color = turtles[i].pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = random.randint(0, 15)
        turtles[i].forward(random_distance)

screen.exitonclick()
