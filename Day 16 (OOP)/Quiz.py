from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
on = True

while on:
    choice = input(f"What would you like? ({menu.get_items()}) ")
    if choice == "off":
        on  = False
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (drink):
            _sufficient = coffee_maker.is_resource_sufficient(drink)
            if _sufficient:
                _transaction_success = money_machine.make_payment(drink.cost)
                if (_transaction_success):
                    coffee_maker.make_coffee(drink)