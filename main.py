from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()
end = False

while not end:
    options = menu.get_items()
    choice = input(f"What would you like? {options}")
    if choice == "off":
        end = True
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            transaction = money_machine.make_payment(drink.cost)
            if transaction:
                coffee_maker.make_coffee(drink)
