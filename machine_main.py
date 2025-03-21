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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Profit: ${profit}")

def turn_off():
    return False

def check_recourses(drink):
    for ingredient, amount in MENU[drink]['ingredients'].items():
        if resources[ingredient] < amount:
            return False
    return True

def make_coffee(drink):
        for ingredient, amount in MENU[drink]['ingredients'].items():
            resources[ingredient] -= amount
        print(f"Here is your {drink}. Enjoy!")


def prompt_user():
    global profit
    while True:
        prompt = input(f"What would you like? (espresso/latte/cappuccino) ").lower()
        if prompt == 'report':
            print_report()

        elif prompt == 'off':
            print("Byeee...")
            return turn_off

        else:
            try:
                if prompt not in MENU.keys():
                    raise ValueError("We don't have such a coffee. Try Again.")
                
                elif check_recourses(prompt):
                    
                    while True:

                        print("Please insert the coins.")
                        total = int(input("How many quarters?: ")) * 0.25
                        total += int(input("How many dimes?: ")) * 0.10
                        total += int(input("How many nickles?: ")) * 0.05
                        total += int(input("How many pennies?: ")) * 0.01

                        if total >= MENU[prompt]['cost']:
                            money_in_change = total - MENU[prompt]['cost']
                            print(f"Here is ${money_in_change} in change.")
                            make_coffee(prompt)
                            profit += MENU[prompt]["cost"]
                            break
                        
                        else:
                            print("Not enough money.")

                else:
                    print(f"Sorry, not enough ingredients.")

            except ValueError as e:
                print(e)

prompt_user()