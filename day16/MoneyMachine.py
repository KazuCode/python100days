class MoneyMachine():

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }


    def __init__(self) -> None:
        self.money = 0
        self.money_inserted = 0


    def report(self):
        print(f'Money: {self.CURRENCY}{self.money}')


    def process_coin(self):
        print('Please insert coins.')
        for coin in self.COIN_VALUES:
            self.money_inserted += int(input(f'How many {coin}?: ')) * self.COIN_VALUES[coin]
        return self.money_inserted


    def make_payment(self, cost: float):
        money_inserted = self.process_coin()
        if money_inserted >= cost:
            change = round(money_inserted - cost, 2)
            print(f'Here is {self.CURRENCY}{change} in change.')
            self.money += cost
            self.money_inserted = 0
            return True
        else:
            print('Sorry, you did not insert enough money... Money refunded.')
            self.money_inserted = 0
            return False