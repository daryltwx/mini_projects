from menu import MENU, resources


resources["money"] = 0.0


# Step 1. Get user's choice
def main():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower().strip()
        match choice:
            case "report":
                get_report()
            case "off":
                exit()
            case "espresso" | "latte" | "cappuccino":
                if check_resources(choice):
                    payment = get_payment()
                    if check_payment(payment, choice):
                        change = "{:.2f}".format(give_change(payment, choice))
                        print(f"Here is ${change} dollars in change.")
                        update_resources(choice)
                        
                        print(f"Here is your {choice}. Enjoy!")
                    else:
                        print("Sorry that's not enough money. Money refunded.")
                else:
                    materials = lack_of_resources(choice)
                    print(f"Sorry there is not enough {materials}. ")
            case _:
                print("Stop fooling around.")

    
def get_report():
    """
    Give a break down of available resources.

    :takes All the current variables.
    :return str
    """
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money = resources["money"]

    print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")


# Step 2. Check if there is enough resources to make user's choice
def check_resources(choice):
    """
    Compares current available required resource, and if after reduction,
    is it greater than zero.
    Loops the ingredients to calculate.

    :takes user choice
    :returns bool
    """
    ingredients = get_ingredients(choice)
    for i in ingredients:
        if resources[i] - ingredients[i] <= 0:
            return False

    return True

def lack_of_resources(choice):
    """
    Compares current available required resource, and if after reduction,
    is it greater than zero.
    Loops the ingredients to calculate.

    :takes user choice
    :returns bool
    """
    ingredients = get_ingredients(choice)
    for i in ingredients:
        if resources[i] - ingredients[i] <= 0:
            return i    

def get_ingredients(choice):
    """
    Gets the ingredients required, in a form of a dict. 

    :takes user choice
    :returns dict
    """
    return MENU[choice]["ingredients"]

# Step 3. If resources is sufficient, start collecting the cost

# if check_resources(choice):
    #get_payment()


def get_payment() -> float:
    """
    Get user input on the number and types of coins as payment.
    Returns calculated amount of coins input.

    :takes None
    :returns float 
    """
    coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
    }
    
    payment = 0
    print("Please insert coins. ")
    for coin in coins:
        user_input = int(input(f"How many {coin}? "))
        payment += (coins[coin] * user_input)
    
    return payment


# Step 4. Check if the amount was sufficient, generate change if excess.
# if not, refund. Add the price of coffee to money variable for the report. 

def check_payment(payment, choice)-> bool:
    """
    Check if transaction is successful. 

    :takes payment, choice
    :return bool
    """
    change = (payment - MENU[choice]["cost"])
    if change >= 0:
        return True
    
    return False

def give_change(payment, choice)-> int:
    """
    Check if transaction is successful. 

    :takes payment, choice
    :return bool
    """
    change = (payment - MENU[choice]["cost"])
    if change >= 0:
        return change

def update_resources(choice) -> None:
    resources["money"] += float((MENU[choice]["cost"]))

    ingredients = get_ingredients(choice)
    for i in ingredients:
        resources[i] -= ingredients[i]




# Step 5.  Generate coffee and update resources. Then deduct the resources for the choice.


# Step 6. Only after all resources have been deducted, tell user, here is their drink. Enjoy.


main()