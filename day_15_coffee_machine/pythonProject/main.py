from fontTools.misc.cython import returns
from numba.core.ir import Global

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

#300
#200
#100

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# print(MENU["espresso"]["ingredients"]["water"])
espresso_water = MENU["espresso"]["ingredients"]["water"]
# print(espresso_water)
# print(MENU["espresso"]["ingredients"]["coffee"])
espresso_coffee = MENU["espresso"]["ingredients"]["coffee"]
# print(espresso_coffee)
# print(MENU["espresso"]["cost"])
espresso_cost = MENU["espresso"]["cost"]
# print(espresso_cost)

latte_water = MENU["latte"]["ingredients"]["water"]
latte_milk = MENU["latte"]["ingredients"]["milk"]
latte_coffee = MENU["latte"]["ingredients"]["coffee"]
latte_cost = MENU["latte"]["cost"]

cappuccino_water = MENU["cappuccino"]["ingredients"]["water"]
cappuccino_milk = MENU["cappuccino"]["ingredients"]["milk"]
cappuccino_coffee = MENU["cappuccino"]["ingredients"]["coffee"]
cappuccino_cost = MENU["cappuccino"]["cost"]

resources_water = resources["water"]
# print(resources_water)
resources_milk = resources["milk"]
resources_coffee = resources["coffee"]

change = 0

# print(resources)

# TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# user_prompt = input("What would you like? (espresso/latte/cappuccino):").lower()

# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
machine_on = True

# if user_prompt == "off":
#     machine_on = False

# TODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
def print_resources():
    print("Current Resources")
    for key in resources:
        print(f"{key}: {resources[key]}")

# print_resources()

# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

def enough_resources():
    if user_prompt == "espresso":
        if resources_water > espresso_water and resources_coffee > espresso_coffee:
            return True
            # print("enough_resources")
        else:
            return False
            # print("not enough_resources")
    elif user_prompt == "latte":
        if resources_water > latte_water and resources_milk > latte_milk and resources_coffee > latte_coffee:
            return True
            # print("enough_resources")
        else:
            return False
            # print("not enough_resources")
    elif user_prompt == "cappuccino":
        if resources_water > cappuccino_water and resources_milk > cappuccino_milk and resources_coffee > cappuccino_coffee:
            return True
            # print("enough_resources")
        else:
            return False
            # print("not enough_resources")

    # print("enough_resources")

# enough_resources()


user_money = 0
# TODO: 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def calculate_coins():
    global user_money
    print("Please insert coins")
    quarters = int(input("How many quarters: ")) * 0.25
    dimes = int(input("How many dimes: ")) * 0.10
    nickles = int(input("How many nickles: ")) * 0.05
    pennies = int(input("How many pennies: ")) * 0.01
    total_coins = round(quarters + dimes + nickles + pennies, 2)
    user_money = total_coins
    # return total_coins

# print(total_coins)
# calculate_coins()
# user_money = calculate_coins()
# print(f"you insert ${user_money}")


# TODO: 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# print(f"change {change}")


def transaction():
    global change
    if user_prompt == "espresso":
        if user_money >= espresso_cost:
            change = round(user_money - espresso_cost, 2)
            return True
        else:
            return False
    elif user_prompt == "latte":
        if user_money >= latte_cost:
            change = round(user_money - latte_cost, 2)
            return True
        else:
            return False

    elif user_prompt == "cappuccino":
        if user_money >= cappuccino_cost:
            change = round(user_money - cappuccino_cost, 2)
            return True
        else:
            return False


# transa = transaction()
# print(transa)
# print(f"change {change}")
# if transaction():
#     print("transa yes")
# else:
#     print("transa no")
#
# print(change)


# TODO: 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.

def  make_coffee():
    if user_prompt == "espresso":
        resources["water"] -= 50
        resources["coffee"] -= 18
    elif user_prompt == "latte":
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
    elif user_prompt == "cappuccino":
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24



while machine_on:
    user_prompt = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_prompt == "off":
        print("Machine goes off, GOODBYE!")
        machine_on = False
    elif user_prompt == "resources":
        print_resources()

    elif user_prompt == "espresso":
        enough_resources()
        if enough_resources():
            print(f"We have enough resources please insert ${espresso_cost}")
        else:
            print("Sorry we dont have enough resources, GOODBYE")
            continue
        calculate_coins()
        print(f"Yoy pay {user_money}")
        transaction()
        if transaction():
            resources["money"] += espresso_cost
            print("You have enough money, nice")
        else:
            print("you dont have enough money")
            continue

        if enough_resources() and transaction():
            make_coffee()
            print(f"you coffe cost {espresso_cost} you pay ${user_money} for it, and here is you change ${change}")

    elif user_prompt == "latte":
        enough_resources()
        if enough_resources():
            print(f"We have enough resources please insert ${latte_cost}")
        else:
            print("Sorry we dont have enough resources, GOODBYE")
            continue
        calculate_coins()
        print(resources["money"])
        print(f"Yoy pay {user_money}")
        transaction()
        if transaction():
            resources["money"] += latte_cost
            print("You have enough money, nice")
        else:
            print("you dont have enough money")
            continue

        if enough_resources() and transaction():
            make_coffee()
            print(f"you coffe cost {latte_cost} you pay ${user_money} for it, and here is you change ${change}")

    elif user_prompt == "cappuccino":
        enough_resources()
        if enough_resources():
            print(f"We have enough resources please insert ${cappuccino_cost}")
        else:
            print("Sorry we dont have enough resources, GOODBYE")
            continue
        calculate_coins()
        print(f"Yoy pay {user_money}")
        transaction()
        if transaction():
            resources["money"] += cappuccino_cost
            print("You have enough money, nice")
        else:
            print("you dont have enough money")
            continue

        if enough_resources() and transaction():
            make_coffee()
            print(f"you coffe cost {cappuccino_cost} you pay ${user_money} for it, and here is you change ${change}")
