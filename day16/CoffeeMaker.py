import MenuItem

class CoffeeMaker():

    def __init__(self) -> None:
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }


    def report(self):
            print(f'Water: {self.resources['water']}ml')
            print(f'Milk: {self.resources['milk']}ml')
            print(f'Coffee: {self.resources['coffee']}g')


    def is_resource_sufficient(self, drink: MenuItem):
        for ingr in drink.ingredients:
            if self.resources[ingr] < drink.ingredients[ingr]:
                 return False
        return True


    def make_coffee(self, order: MenuItem):
        for ingr in order.ingredients:
            self.resources[ingr] -= order.ingredients[ingr]
        print(f'Your {order.name} is served, enjoy!')