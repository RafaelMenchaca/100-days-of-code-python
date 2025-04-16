from turtle import Screen
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.shape("turtle")

angles = [0, 90, 180, 270]
tim.speed(0)
tim.pensize(3)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_c = (r,g,b)
    return random_c

def draw_circle(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_circle(1)


screen = Screen()
screen.exitonclick()