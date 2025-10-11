# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(235, 252, 244), (199, 12, 32), (249, 236, 25), (244, 248, 253), (40, 77, 187), (239, 229, 4), (38, 217, 69), (227, 160, 50), (29, 40, 156), (213, 75, 14), (17, 153, 17), (242, 35, 160), (196, 16, 11), (68, 10, 31), (223, 21, 120), (61, 15, 8), (223, 141, 207), (11, 97, 62), (221, 159, 9), (53, 210, 230), (19, 21, 48), (75, 72, 218), (238, 156, 218), (10, 228, 239), (75, 211, 167), (89, 234, 199), (224, 84, 45), (59, 233, 242)]
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(15, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()