from menu import MENU, resources

money = 0.00

def report(money):
    """ Takes money and return the report status of the machine"""
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}"

# TODO 4: Check resources
def check_resources(choice, item):
    ingredient = MENU[choice]["ingredients"][item]
    print(ingredient)


def check_ingredients(drink):
    ingredients = drink["ingredients"]
    for i in ingredients:
        cost = resources[i]
        if cost <= 0:
            print(f"Sorry there is not enough {i}")
            exit()
        else:
            cost = (resources[i] - ingredients[i])
            print(cost)
            print(i)

# TODO 1: Prompt user for drink
choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
drink = MENU[choice]
check_ingredients(drink)

# Check resources 


# TODO 2: Turn off machine with off prompt
if choice == "off":
    exit()

# TODO 3: Print report with report prompt
if choice == "report":
    print(report(money))



# TODO 5: Process coins

# TODO 6: Check if transaction is successful

# TODO 7: Make coffee
