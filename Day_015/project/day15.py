MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 300,
}

money = 0.0


def print_report():
    print("\n----- REPORT -----")
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")
    print("------------------\n")


def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        if resources[item] < ingredients[item]:
            print(f"Sorry there is not enough {item}.")
            return False

    return True


def process_coins():
    print("\nPlease insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total = (
        quarters * 0.25
        + dimes * 0.10
        + nickels * 0.05
        + pennies * 0.01
    )

    return total


def transaction_successful(money_received, drink_cost):
    global money

    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False

    change = round(money_received - drink_cost, 2)

    if change > 0:
        print(f"Here is ${change:.2f} in change.")

    money += drink_cost
    return True


def make_coffee(drink):
    ingredients = MENU[drink]["ingredients"]

    for item in ingredients:
        resources[item] -= ingredients[item]

    print(f"Here is your {drink}. Enjoy!\n")


machine_on = True

while machine_on:

    choice = input(
        "What would you like? (espresso/latte/cappuccino): "
    ).lower()

    if choice == "off":
        machine_on = False
        print("Coffee machine turned off.")

    elif choice == "report":
        print_report()

    elif choice in MENU:

        if check_resources(choice):

            payment = process_coins()

            if transaction_successful(
                payment,
                MENU[choice]["cost"]
            ):
                make_coffee(choice)

    else:
        print("Invalid choice. Please try again.")