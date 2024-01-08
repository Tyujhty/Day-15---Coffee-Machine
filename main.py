from data import MENU, resources


def check_choice(consumer_choice):
    coffee_data = {}
    for coffee in MENU:
        if consumer_choice == coffee:
            coffee_data = MENU[coffee]
            return coffee_data


def check_resources(coffee_selection):
    coffer_ingredients = coffee_selection['ingredients']
    missing_ingredient = []
    for ingredient in coffer_ingredients:
        if coffer_ingredients[ingredient] > resources[ingredient]:
            missing_ingredient.append(ingredient)
    if missing_ingredient:
        print(f"Sorry there is not enough {', '.join(missing_ingredient)}.")
    else:
        for ingredient in coffer_ingredients:
            resources[ingredient] -= coffer_ingredients[ingredient]
            return resources


def insert_coin():
    quarter = int(input("How many quarters?: ")) * 0.25
    dime = int(input("How many dimes: ")) * 0.10
    nickle = int(input("How many nickels?: ")) * 0.05
    penny = int(input("How many pennies?: ")) * 0.25

    total_pay = quarter + dime + nickle + penny

    return total_pay


def pay_coffee(coffee_selection):

    price_coffee = coffee_selection['cost']

    print(f"{price_coffee}$, please insert coins.")

    total_pay = insert_coin()

    total_change = total_pay - price_coffee

    if total_pay > price_coffee:
        print(f"Here is ${total_change} in change.")
    elif total_pay < price_coffee:
        print(f"You have to complete ${total_change} in change, please insert coin.")
        complete_total = 0
        while complete_total > total_change:
            complete_total = insert_coin()
            print(complete_total, total_change)
            insert_coin()

        print("Here's your coffee")


def coffee_machine():
    consumer_choice = input("What would you like?: (espresso/latte/cappuccino): ")
    if consumer_choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")
        coffee_machine()
    else:
        coffee_selection = check_choice(consumer_choice)
        check_resources(coffee_selection)
        pay_coffee(coffee_selection)


coffee_machine()