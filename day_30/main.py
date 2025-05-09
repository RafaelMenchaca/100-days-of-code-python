# with open("a_file.txt") as file:
#     file.read()
from openpyxl.cell.cell import TYPE_ERROR

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["asdq"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError("this is an error that i made up")


# height = float(input("Height: "))
# weight = int(input("Weight: "))
#
# if height > 2:
#     raise ValueError("Human Height should not be over 3 meters.")
#
#
# bmi = weight / height ** 2
# print(bmi)

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")

try:
    make_pie(4)
except:
    print("Fruit pie")
