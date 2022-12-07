import data
import os
import logo

resources = data.resources
drink = data.MENU
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
espresso = drink["espresso"]
latte = drink["latte"]
cappuccino = drink["cappuccino"]
start = True
os.system('cls')
print(logo.logo)
while start:
    what = input("What would you like? (espresso/latte/cappuccino): ")
    correct = False
    while not correct:
        if what == "off":
            start = False
            correct = True
        elif what == "espresso":
            espresso_ing = espresso["ingredients"]
            if water >= espresso_ing["water"] and coffee >= espresso_ing["coffee"]:
                print("Please insert coins:")
                money_pennies = float(input("How many pennies?: "))
                money_nickles = float(input("How many nickles?: "))
                money_dimes = float(input("How many dimes?: "))
                money_quarters = float(input("How many pennies?: "))
                money = round(money_pennies * 0.01 + money_nickles * 0.05 + money_dimes * 0.1 + money_quarters * 0.25,
                              2)
                if money >= espresso["cost"]:
                    water = water - espresso_ing["water"]
                    coffee = coffee - espresso_ing["coffee"]
                    money = round(money - espresso["cost"], 2)
                    if money > 0:
                        print(f"Here is ${money} in change.")
                        money=0
                    print("Here is your espresso ☕. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    money = 0
            elif water < espresso_ing["water"]:
                print("Sorry, there is not enough water.")
            elif coffee < espresso_ing["coffee"]:
                print("Sorry, there is not enough coffee.")
            elif money < espresso["cost"]:
                print("Sorry, there is not enough money.")
            correct = True
        elif what == "latte":
            latte_ing = latte["ingredients"]
            if water >= latte_ing["water"] and coffee >= latte_ing["coffee"] and milk >= latte_ing["milk"]:
                print("Please insert coins:")
                money_pennies = float(input("How many pennies?: "))
                money_nickles = float(input("How many nickles?: "))
                money_dimes = float(input("How many dimes?: "))
                money_quarters = float(input("How many pennies?: "))
                money = round(money_pennies*0.01 + money_nickles*0.05 + money_dimes*0.1 + money_quarters*0.25, 2)
                if money >= latte["cost"]:
                    water = water - latte_ing["water"]
                    coffee = coffee - latte_ing["coffee"]
                    milk = milk - latte_ing["milk"]
                    money = round(money - latte["cost"], 2)
                    if money > 0:
                        print(f"Here is ${money} in change.")
                        money = 0
                    print("Here is your latte ☕. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    money = 0
            elif water < latte_ing["water"]:
                print("Sorry, there is not enough water.")
            elif coffee < latte_ing["coffee"]:
                print("Sorry, there is not enough coffee.")
            elif milk < latte_ing["milk"]:
                print("Sorry, there is not enough milk.")
            elif money < latte["cost"]:
                print("Sorry, there is not enough money.")
            correct = True
        elif what == "cappuccino":
            capp_ing = cappuccino["ingredients"]
            if water >= capp_ing["water"] and coffee >= capp_ing["coffee"] and milk >= capp_ing["milk"]:
                print("Please insert coins:")
                money_pennies = float(input("How many pennies?: "))
                money_nickles = float(input("How many nickles?: "))
                money_dimes = float(input("How many dimes?: "))
                money_quarters = float(input("How many pennies?: "))
                money = round(money_pennies * 0.01 + money_nickles * 0.05 + money_dimes * 0.1 + money_quarters * 0.25,
                              2)
                if money >= cappuccino["cost"]:
                    water = water - capp_ing["water"]
                    coffee = coffee - capp_ing["coffee"]
                    milk = milk - capp_ing["milk"]
                    money = round(money - cappuccino["cost"], 2)
                    if money > 0:
                        print(f"Here is ${money} in change.")
                        money = 0
                    print("Here is your latte ☕. Enjoy!")
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    money = 0
            elif water < capp_ing["water"]:
                print("Sorry, there is not enough water.")
            elif coffee < capp_ing["coffee"]:
                print("Sorry, there is not enough coffee.")
            elif milk < capp_ing["milk"]:
                print("Sorry, there is not enough milk.")
            elif money < cappuccino["cost"]:
                print("Sorry, there is not enough money.")
            correct = True
        elif what == "report":
            print(f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g")
            print(f"Money: ${money}")
            correct = True
        else:
            what = input("Insert a correct answer: ")
