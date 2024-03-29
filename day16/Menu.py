import MenuItem

class Menu():

    def __init__(self):
        self.menu = [
            MenuItem.MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem.MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem.MenuItem(name="cappuccino", water=250, milk=50, coffee=24, cost=3)
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f'{ item.name }/'
        return options
    

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print('Sorry, we did not find your order.')