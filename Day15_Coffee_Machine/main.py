from data import MENU


# Check the coins and gives the change
# If not enough money is put, reject the transaction
def check_money(amount, drink_price):
    """Returns True if the payment is enough for the drink, or False if it is insufficient."""
    if amount < drink_price:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(amount - drink_price, 2)
    if change > 0:
        print(f"Here is ${change} in change.")
    resources['money'] += drink_price
    return True


# Check if resources are sufficient
def check_resources(drink_ingredients):
    """Compares the ingredients against the resources and returns a boolean"""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True


def make_drink(drink_name, drink_ingredients):
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"Here is your {drink_name} {MENU[drink_name]['emoji']} Enjoy!")


def print_resources():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
        "money": 0
}

machine_is_on = True

while machine_is_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "off":
        machine_is_on = False
    elif order == "report":
        # Print a report with the resources
        print_resources()
    elif order in MENU:
        drink = MENU[order]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if check_money(payment, drink['price']):
                make_drink(order, drink['ingredients'])
    else:
        print("Wrong order, please select again.")
