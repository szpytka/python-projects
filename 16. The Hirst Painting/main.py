# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# color_palette = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_palette.append(new_color)
# print(color_palette)

from turtle import Turtle
from turtle import Screen
import random

color_list = [(206, 159, 106), (124, 168, 193), (50, 108, 144),
              (158, 86, 50), (178, 161, 37), (189, 144, 165), (141, 67, 96), (131, 178, 158), (224, 203, 122),
              (53, 123, 89),
              (141, 24, 47), (66, 19, 41), (20, 38, 72), (188, 87, 115), (42, 165, 187), (67, 163, 133), (214, 89, 60),
              (65, 23, 13),
              (225, 170, 190), (14, 98, 59), (145, 28, 18), (153, 212, 198), (32, 55, 116), (12, 56, 30),
              (105, 118, 171),
              (235, 172, 160)]

my_screen = Screen()
my_screen.colormode(255)
timmy = Turtle()
timmy.hideturtle()
timmy.penup()
timmy.speed(0)
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

my_screen.exitonclick()
