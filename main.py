from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


coffee_names = menu.get_items()
coffee_costs = menu

while True:
    choice = input(f"What do you want? {coffee_names}: ")
    drink = menu.find_drink(choice)


    if choice not in coffee_names:
        drink

    elif choice.lower() == "report":
        print(coffee_maker.report())
        print(money_machine.report())

    else:
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)











