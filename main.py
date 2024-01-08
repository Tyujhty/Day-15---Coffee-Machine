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

consumer_choice = input("What would you like?: (espresso/latte/cappuccino): ")
coffee_selection = check_choice(consumer_choice)

check_resources(coffee_selection)
