# from turtle import Turtle, Screen
#
# tim = Turtle()
# screen = Screen()
#
# def move_forwards():
#     tim.forward(30)
# def move_backwards():
#     tim.backward(30)
# def rotate_right():
#     tim.right(10)
# def rotate_left():
#     tim.left(10)
# def pen_up():
#     tim.penup()
# def pen_down():
#     tim.pendown()
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.speed(0)
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="d", fun=rotate_right)
# screen.onkey(key="a", fun=rotate_left)
# screen.onkey(key="u", fun=pen_up)
# screen.onkey(key="x", fun=pen_down)
# screen.onkey(key="c", fun=clear)
#
# screen.exitonclick()
import random
import turtle
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will "
                                               "win the race? Enter the color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-140, -80, -20, 40, 100, 160]
all_turtles = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)
#     print(turtle.color())
#     print(all_turtles)
#
# print(all_turtles)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            print(turtle.color())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} turtle is the winner")
            else:
                print(f"You've lost! the {winning_color} win")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


#
# juan = Turtle(shape="turtle")
# juan.color(random.choice(colors))
# juan.penup()
# juan.goto(x=-230, y=-80)
#
# iram = Turtle(shape="turtle")
# iram.color(random.choice(colors))
# iram.penup()
# iram.goto(x=-230, y=-20)
#
# sampi = Turtle(shape="turtle")
# sampi.color(random.choice(colors))
# sampi.penup()
# sampi.goto(x=-230, y=40)
#
# hacha = Turtle(shape="turtle")
# hacha.color(random.choice(colors))
# hacha.penup()
# hacha.goto(x=-230, y=100)
#
# nana = Turtle(shape="turtle")
# nana.color(random.choice(colors))
# nana.penup()
# nana.goto(x=-230, y=160)
#
#


screen.exitonclick()