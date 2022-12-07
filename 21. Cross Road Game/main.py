import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

d = 0
i = 0
level = 1
cars = []
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")

speed = STARTING_MOVE_DISTANCE
car_creation = 6
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    d += 1
    # car creation
    if d % car_creation == 0:
        cars.append(CarManager())
        cars[i].position()
        i += 1
    # car movement
    for car in cars:
        car.car_movement(speed)
        if car.xcor() < -320:
            car.hideturtle()
        # turtle collision with car
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False
        # turtle finish line
        if player.ycor() == FINISH_LINE_Y:
            player.starting_position()
            speed += MOVE_INCREMENT
            level += 1
            scoreboard.score(level)
            if level % 3 == 0 and car_creation > 0:
                car_creation -= 1

screen.exitonclick()
