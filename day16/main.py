import CoffeeMaker, Menu, MenuItem, MoneyMachine

menu = Menu.Menu()
coffeemaker = CoffeeMaker.CoffeeMaker()
moneymachine = MoneyMachine.MoneyMachine()
machine_on = True

while machine_on:
    choice = input(f'What would you like? {menu.get_items()}').lower()
    if choice == 'report':
        coffeemaker.report()
        moneymachine.report()
    elif choice == 'off':
        machine_on = False
    else:
        beverage = menu.find_drink(choice)
        if beverage != None and coffeemaker.is_resource_sufficient(beverage) and moneymachine.make_payment(beverage.cost):
                    coffeemaker.make_coffee(beverage)
