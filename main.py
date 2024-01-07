from data import MENU


def check_choice(consumer_choice):
    coffee_data = {}
    for coffee in MENU:
        if consumer_choice == coffee:
            coffee_data = MENU[coffee]
            return coffee_data

consumer_choice = input("What would you like?: (espresso/latte/cappuccino): ")
coffee_selection = check_choice(consumer_choice)
print(coffee_selection)
