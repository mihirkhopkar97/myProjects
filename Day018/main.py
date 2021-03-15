from turtle import Turtle, Screen
from random import randint

timmy = Turtle('turtle')
timmy.color('green')


def draw_square():
    for _ in range(4):
        timmy.forward(100)
        timmy.right(90)


def draw_dashed_line():
    for _ in range(50):
        timmy.forward(5)
        timmy.penup()
        timmy.forward(5)
        timmy.pendown()


def draw_multiple_shapes():
    for sides in range(4, 11):
        if sides % 2 == 0:
            timmy.pencolor('green')
        else:
            timmy.pencolor('red')
        for _ in range(sides):
            timmy.forward(50)
            timmy.right(360/sides)


def random_walk():
    lines = 1
    while lines < 100:
        random_number = randint(1, 4)
        if random_number == 1:
            timmy.pencolor('green')
            timmy.forward(10)
            timmy.left(90)
        elif random_number == 2:
            timmy.pencolor('yellow')
            timmy.right(90)
            timmy.forward(10)
        elif random_number == 3:
            timmy.pencolor('blue')
            timmy.left(90)
            timmy.forward(10)
        else:
            timmy.pencolor('red')
            timmy.forward(10)
            timmy.right(90)
        timmy.pensize(lines % random_number)
        timmy.speed(lines)
        lines += 1

def draw_spirograph():
    while True:
        timmy.circle(50)
        timmy.left(10)

import colorgram
draw_spirograph()






screen = Screen()
screen.exitonclick()