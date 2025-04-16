from turtle import Turtle, Screen
import turtle as t

import random

from numba.core.ir import Global
from pyasn1_modules.rfc2985 import signingDescription

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")

# tim.color("red")
# colores = "red", "blue", "gray", "black", "yellow", "green", ""
#
# forms = {
#     "triangle": {
#         "degrees": 120,
#         "sides": 3
#     },
#     "square": {
#         "degrees": 90,
#         "sides": 4
#     },
#     "pentagon": {
#         "degrees": 72,
#         "sides": 5
#     },
#     "hexagon": {
#         "degrees": 60,
#         "sides": 6
#     },
#     "heptagon": {
#         "degrees": 51.43,
#         "sides": 7
#     },
#     "octagon": {
#         "degrees": 45,
#         "sides": 8
#     },
#     "nonagon": {
#         "degrees": 40,
#         "sides": 9
#     },
#     "decagon": {
#         "degrees": 36,
#         "sides": 10
#     },
# }
#
# for i in forms:
#     tim.color(random.choice(colores))
#     for d in range(forms[i]["sides"]):
#         tim.forward(100)
#         tim.right(forms[i]["degrees"])

# colors = ["red", "blue", "pink", "yellow", "green", "gray", "brown", "red"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for b in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

# colors = ["red", "blue", "pink", "yellow", "green", "gray", "brown", "red"]
angles = [0, 90, 180, 270]

tim.speed(0)
tim.pensize(10)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_c= (r, g, b)
    return random_c


def random_move():
    tim.color(random_color())
    tim.setheading(random.choice(angles))
    tim.forward(20)

for i in range(200):
    random_move()

screen = Screen()
screen.exitonclick()