status = {"water": 400, "milk": 540, "coffee_beans": 120, "cups": 9, "money": 550}

while True:

    def machine_status():
        print("The coffee machine has:")
        print(status["water"], "ml of water")
        print(status["milk"], "ml of milk")
        print(status["coffee_beans"], "g of coffee beans")
        print(status["cups"], "disposable cups")
        print(f"${status['money']} of money")


    def choice():
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            buy_coffee()
        elif action == "fill":
            fill_machine()
        elif action == "take":
            take_action()
        elif action == "remaining":
            machine_status()
        elif action == "exit":
            quit()


    def buy_coffee():
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
        what_to_buy = input()
        print()
        if what_to_buy == "1":
            if status["water"] >= 250 and status["coffee_beans"] >= 16 and status["cups"] >= 1:
                status["water"] -= 250
                status["coffee_beans"] -= 16
                status["money"] += 4
                status["cups"] -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough resources")

        elif what_to_buy == "2":
            if status["water"] >= 350 and status["milk"] >= 75 and status["coffee_beans"] >= 20 and status["cups"] >= 1:
                status["water"] -= 350
                status["milk"] -= 75
                status["coffee_beans"] -= 20
                status["money"] += 7
                status["cups"] -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough resources")

        elif what_to_buy == "3":
            if status["water"] >= 200 and status["milk"] >= 100 and status["coffee_beans"] >= 12 and status[
                "cups"] >= 1:
                status["water"] -= 200
                status["milk"] -= 100
                status["coffee_beans"] -= 12
                status["money"] += 6
                status["cups"] -= 1
                print("I have enough resources, making you a coffee!")
            else:
                print("Sorry, not enough resources")

        elif what_to_buy == "back":
            choice()


    def fill_machine():
        print("Write how many ml of water you want to add:")
        add_water = int(input())
        status["water"] += add_water
        print("Write how many ml of milk you want to add:")
        add_milk = int(input())
        status["milk"] += add_milk
        print("Write how many grams of coffee beans you want to add:")
        add_coffee_beans = int(input())
        status["coffee_beans"] += add_coffee_beans
        print("Write how many disposable cups of coffee you want to add:")
        add_cups = int(input())
        status["cups"] += add_cups


    def take_action():
        print(f"I gave you ${status['money']}")
        status["money"] -= status["money"]


    choice()