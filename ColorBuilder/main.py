import turtle
import random
from colorextractor import rgb_colors

timmy = turtle.Turtle()
screen = turtle.Screen()
timmy.shape("turtle")
timmy.speed(0)
timmy.penup()
timmy.goto(-230, -230)


def single_line():
    for num in range(11):
        timmy.dot(20, rgb_colors[random.randint(0, 7)])
        timmy.forward(45)


xy = [-230, -180]


def new_line():
    timmy.goto(-230, xy[1])
    timmy.setheading(0)
    xy[1] += 50


x = 0
while x < 10:
    single_line()
    new_line()
    x += 1

timmy.ht()
screen.exitonclick()
