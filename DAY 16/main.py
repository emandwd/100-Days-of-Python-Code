from Menu_Item import Menu
from Coffee_Maker import CoffeeMaker
from Money_Machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_on = True
menu = Menu()

while is_on :
    options = menu.get_items()
    choice = input(f"What would you like?{options} ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else :
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink) :
            print(money_machine.make_drink(drink))
