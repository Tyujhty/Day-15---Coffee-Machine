from data import MENU, resources


def check_choice(consumer_choice):
    coffee_data = {}
    for coffee in MENU:
        if consumer_choice == coffee:
            coffee_data = MENU[coffee]
            return coffee_data

def check_resources(coffee_selection):
    for ingredient in coffee_selection['ingredients']:
        if coffee_selection['ingredients'][ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
        else:
            resources[ingredient] = resources[ingredient] - coffee_selection['ingredients'][ingredient]
            print(resources[ingredient])

consumer_choice = input("What would you like?: (espresso/latte/cappuccino): ")
coffee_selection = check_choice(consumer_choice)

check_resources(coffee_selection)
