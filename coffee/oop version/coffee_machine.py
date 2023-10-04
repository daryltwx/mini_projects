from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
# is_resources_sufficient()

# process_coins()

# is_transaction_sufficient()

# make_coffee()

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        exit()
    elif choice == "report":
        print(coffee_maker.report())
        money_machine.report()