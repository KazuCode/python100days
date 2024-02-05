import data

def print_report():
    print(f'Water: {data.resources['water']}ml')
    print(f'Milk: {data.resources['milk']}ml')
    print(f'Coffee: {data.resources['coffee']}g')
    print(f'Money: ${data.money}')


def insert_money(choice):
    print('Please insert coins.')
    quarters = int(input('How many quarters? '))
    dimes = int(input('How many dimes? '))
    nickels = int(input('How many nickels? '))
    pennies = int(input('How many pennies? '))
    total = round(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01, 2)
    print(f'You inserted ${total}.')
    return total


def calculate_change(money, choice):
    change = round(money - data.MENU[choice]['cost'], 2)
    return change


def check_ingredients(choice):
    for ingr in data.MENU[choice]['ingredients']:
        if data.resources[ingr] < data.MENU[choice]['ingredients'][ingr]:
            return False
    return True


def prepare_beverage(choice):
    data.money += data.MENU[choice]['cost']
    for ingr in data.MENU[choice]['ingredients']:
        data.resources[ingr] -= data.MENU[choice]['ingredients'][ingr]
    print(f'Here is your {choice}!')


machine_on = True

while machine_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice in ['espresso', 'latte', 'cappuccino']:
        if check_ingredients(choice):
            total = insert_money(choice)
            if total >= data.MENU[choice]['cost']:
                change = calculate_change(total, choice)
                print(f'Here is {change} in change.') if change > 0 else ('No change.')
                prepare_beverage(choice)
            else:
                print('Sorry, you did not insert enough money.')
        else:
            print('Sorry, we miss ingredients to prepare your beverage...')
    elif choice == 'report':
        print_report()
    elif choice == 'exit':
        machine_on = False
    else:
        print('Sorry, I did not understand your choice.')