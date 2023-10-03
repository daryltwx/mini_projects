from menu import MENU, resources

money = 0.00
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]


# Step 1. Get user's choice
def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        # Step 1.1 Support for report
        if choice == "report":
            get_report(money, water, milk, coffee)

        # Step 1.2 Support for off
        if choice == "off":
            exit()

        print(check_resources(choice))
    
def get_report(money, water, milk, coffee):
    """
    :takes All the current variables.
    :return str
    """
    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")




# Step 2. Check if there is enough resources to make user's choice
def check_resources(choice, water, milk, coffee):
    """
    :takes user choice
    :returns bool
    """
    ingredients = get_ingredients(choice)
    for i in ingredients:
        if resources[i] - ingredients[i] <= 0:
            return False
    
    return True
        


def get_ingredients(choice):
    """
    :takes user choice
    :returns dict
    """
    return MENU[choice]["ingredients"]

# Step 3. If resources is sufficient, start collecting the cost

# Step 4. Check if the amount was sufficient, generate change if excess.
# if not, refund. Add the price of coffee to money variable for the report. 

# Step 5.  Generate coffee and update resources. Then deduct the resources for the choice.

# Step 6. Only after all resources have been deducted, tell user, here is their drink. Enjoy.


main()