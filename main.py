art = """
        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

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
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def task(coffee):
    for key in MENU[coffee]["ingredients"].keys():
        resources[key] -= MENU[coffee]["ingredients"][key]
        if resources[key] < 0:
            return key
    return True


def coin(price):
    quarter = int(input("How many quarter?: "))
    dime = int(input("How many dime?: "))
    nickle = int(input("How many nickle?: "))
    penny = int(input("How many penny?: "))
    total = quarter * 0.25 + dime * 0.1 + nickle * 0.05 + penny * 0.01
    if price == total:
        return 0
    elif price > total:
        return -1
    else:
        return total - price


run = True
print(art)
while run:
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input in MENU.keys():
        reply = task(user_input)
        if reply is True:
            change = coin(MENU[user_input]["cost"])
            if change == 0:
                print(f"Thank you! Here is your {user_input}")
            elif change > 0:
                print(f"Thank you! Here is your ${change} change and {user_input}")
            else:
                print(f"Not enough fund!")
        else:
            print(f"Not enough {reply}")
    elif user_input == "report":
        for name, quantity in resources.items():
            print(f"{name}: {quantity}")
    elif user_input == "off":
        run = False
    else:
        print("Invalid input. Please try again.")
