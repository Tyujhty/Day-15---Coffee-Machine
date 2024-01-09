from data import MENU, resources


def check_choice(consumer_choice):
    coffee_data = {}
    for coffee in MENU:
        if consumer_choice == coffee:
            coffee_data = MENU[coffee]
            return coffee_data


def check_resources(coffee_selection):
    coffee_ingredients = coffee_selection['ingredients']
    missing_ingredient = []
    for ingredient in coffee_ingredients:
        if coffee_ingredients[ingredient] > resources[ingredient]:
            missing_ingredient.append(ingredient)
    if missing_ingredient:
        print(f"Sorry there is not enough {', '.join(missing_ingredient)}.")
    else:
        for ingredient in coffee_ingredients:
            resources[ingredient] -= coffee_ingredients[ingredient]
        return resources, True


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

    if total_pay > price_coffee or total_pay == price_coffee:
        if total_pay > price_coffee:
            resources['money'] -= total_change
            print(f"Here is ${total_change} in change.")
        print("Here's your coffee ☕")
        return resources['money']

    elif total_pay < price_coffee:
        print("Sorry that's not enough money. Money refunded")
        pay_coffee(coffee_selection)


def coffee_machine():
    consumer_choice = input("What would you like?: (espresso/latte/cappuccino): ")
    if consumer_choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${resources['money']}")
        coffee_machine()
    elif consumer_choice == 'off':
        print("The coffee machine will shut down.")
    else:
        coffee_selection = check_choice(consumer_choice)
        check_resources(coffee_selection)
        if check_resources(coffee_selection):
            pay_coffee(coffee_selection)
            coffee_machine()

coffee_machine()
