class MenuItem():

    def __init__(self, name: str, cost: float, water: int, milk: int, coffee: int):
        self.name           = name
        self.cost           = cost
        self.ingredients    = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }