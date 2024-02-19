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

power = True
while power:


    def get_input():
        global power
        drink = input("What would you like? (espresso/latte/cappuccino)")
        if drink in MENU:
            if check_resources(drink):
                change = get_change()
                if check_change(change, drink):
                    update_resources(MENU[drink])
                    print(f"Here is your {drink} Enjoy!")
        elif drink == 'report':
            return print_resources()
        elif drink == 'off':
            power = False


    def print_resources():
        for resource, amount in resources.items():
            print(f"{resource.title():} {amount}ml" if resource != "coffee" else f"{resource.title():} {amount}g")
        print(f"Money: ${profit}")


    def check_resources(drink):
        for item, required_amount in MENU[drink]['ingredients'].items():
            if resources[item] < required_amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True


    def get_change():
        print("please Insert Your Coins")
        quarters = int(input('How many Quarters?'))
        dimes = int(input('How many Dimes?'))
        nickles = int(input('How many Nickles?'))
        pennies = int(input('How many pennies?'))
        return(quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01)


    def check_change(change, drink):
        if change < MENU[drink]['cost']:
            print("Sorry, that's not enough money. Money refunded.")
            return False
        else:
            print(f"Here is ${change - MENU[drink]['cost']:.2f} in change.")
            return True

    def update_resources(drink):
        global profit
        for ingredient, amount in drink["ingredients"].items():
            resources[ingredient] -= amount
        profit += drink['cost']


    get_input()