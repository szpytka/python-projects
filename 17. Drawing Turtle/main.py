from turtle import Turtle, Screen

tim = Turtle("turtle")
tim.pensize(5)
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.backward(20)


def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="a", fun=left)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=right)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
