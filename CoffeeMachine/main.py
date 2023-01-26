from data import menu
from data import resources
on = True
empty = False


def calculate_change(drink):
    print(f"The cost is ${menu[drink]['cost']}.")
    while True:
        try:
            quarters = int(input("How many quarters? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            dimes = int(input("How many dimes? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    while True:
        try:
            nickels = int(input("How many nickels? "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    cents_given = (quarters * 25) + (dimes * 10) + (nickels * 5)
    change = ((menu[drink]['cost'] * 100) - cents_given)
    print(f"Your change is {change}.")


def calculate_ingredients(drink):
    global empty
    for ingredient in resources:
        resources[ingredient] -= menu[drink]["ingredients"][ingredient]
        if resources[ingredient] < 0:
            if drink == "espresso" and resources[ingredient] == "milk":
                empty = False
            else:
                resources[ingredient] += menu[drink]["ingredients"][ingredient]
                print(f"Sorry, there is not enough {ingredient}. Please refill.")
                empty = True


while on:
    prompt = input("What would you like? Please type your answer. (espresso, latte, or cappuccino) ")
    for option in menu:
        if prompt == option:
            calculate_ingredients(option)
            if not empty:
                calculate_change(option)
                print("Your drink should be done soon.")
    if prompt == "report":
        print(f"Water = {resources['water']} \nMilk = {resources['milk']} \nCoffee = {resources['coffee']}")
    if prompt == "off":
        on = False
