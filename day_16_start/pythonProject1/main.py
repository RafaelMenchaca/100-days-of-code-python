# import turtle
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
#
# def triangle():
#     for i in range(3):
#         timmy.forward(100)
#         timmy.left(120)
#
# def square():
#     for i in range(4):
#         timmy.forward(100)
#         timmy.left(90)
#
# # triangle()
# # square()
# # timmy.forward(100)
# # timmy.left(120)
# # timmy.forward(100)
# # timmy.left(120)
#
#
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

import prettytable
from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["Pokemon Names", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "c"
print(table)
