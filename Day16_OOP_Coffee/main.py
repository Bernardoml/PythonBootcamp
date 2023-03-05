from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
cash_register = MoneyMachine()
menu = Menu()
machine_is_on = True

while machine_is_on:
    order = input(f"What would you like? {menu.get_items()}: ").lower()

    if order == "off":
        machine_is_on = False
    elif order == "report":
        # Print a report with the resources
        coffee_machine.report()
        cash_register.report()
    elif menu.find_drink(order):
        drink_ordered = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(drink_ordered):
            if cash_register.make_payment(drink_ordered.cost):
                coffee_machine.make_coffee(drink_ordered)
    else:
        print("Wrong order, please select again.")
