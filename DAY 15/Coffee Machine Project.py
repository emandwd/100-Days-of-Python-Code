from menu import MENU

total_water = 300
total_milk = 200
total_coffee = 100
total_money = 0
user_money = 0
remainder = 0

def report():
    print(f"Water = {total_water}ml \nMilk = {total_milk}ml \nCoffee = {total_coffee}g \nMoney = ${total_money}")

def Process_Coins(user_choice):
    global total_money
    global user_money
    print("Please insert coins. ")
    quarters_to_dollars = int(input("How many quarters? "))*0.25
    dimes_to_dollars = int(input("How many dimes? "))*0.10
    nickels_to_dollars = int(input("How many nickles? "))*0.05
    pennies_to_dollars = int(input("How many pennies? "))*0.01
    user_money = quarters_to_dollars + dimes_to_dollars + nickels_to_dollars + pennies_to_dollars
    if user_money < MENU[user_choice]["cost"] :
        print("Sorry, that's not enough money. Money refunded.")
        return False # if we used return, the calculation function will keep running

    if user_money > MENU[user_choice]["cost"] :
        remainder = round(user_money - MENU[user_choice]["cost"],2)
        print(f"Here is ${remainder} in change.")

    total_money += MENU[user_choice]["cost"]
    print(f"Here is your {user_choice} ☕. Enjoy!")
    return True


def calculations(user_choice):
    global total_water, total_milk, total_coffee, total_money

    # Check resources first
    if user_choice == "espresso":
        if total_water < MENU["espresso"]["ingredients"]["water"]:
            print("Not enough water.")
            return
        if total_coffee < MENU["espresso"]["ingredients"]["coffee"]:
            print("Not enough coffee.")
            return

    elif user_choice == "latte":
        if total_water < MENU["latte"]["ingredients"]["water"]:
            print("Not enough water.")
            return
        if total_coffee < MENU["latte"]["ingredients"]["coffee"]:
            print("Not enough coffee.")
            return
        if total_milk < MENU["latte"]["ingredients"]["milk"]:
            print("Not enough milk.")
            return

    elif user_choice == "cappuccino":
        if total_water < MENU["cappuccino"]["ingredients"]["water"]:
            print("Not enough water.")
            return
        if total_coffee < MENU["cappuccino"]["ingredients"]["coffee"]:  # FIXED typo
            print("Not enough coffee.")
            return
        if total_milk < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Not enough milk.")
            return

    success = Process_Coins(user_choice)
    if not success:
        return

    if user_choice == "espresso":
        total_water -= MENU["espresso"]["ingredients"]["water"]
        total_coffee -= MENU["espresso"]["ingredients"]["coffee"]

    elif user_choice == "latte":
        total_water -= MENU["latte"]["ingredients"]["water"]
        total_coffee -= MENU["latte"]["ingredients"]["coffee"]
        total_milk -= MENU["latte"]["ingredients"]["milk"]

    elif user_choice == "cappuccino":
        total_water -= MENU["cappuccino"]["ingredients"]["water"]
        total_coffee -= MENU["cappuccino"]["ingredients"]["coffee"]
        total_milk -= MENU["cappuccino"]["ingredients"]["milk"]


while True:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        report()
        continue
    if user_choice == "off":
        break

    calculations(user_choice)




