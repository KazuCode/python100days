def add(first_nbr: int, second_nbr: int):
    return first_nbr + second_nbr

def subtract(first_nbr: int, second_nbr: int):
    return first_nbr - second_nbr

def multiply(first_nbr: int, second_nbr: int):
    return first_nbr * second_nbr

def divide(first_nbr: int, second_nbr: int):
    return round(first_nbr / second_nbr, 2)

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    first_number = int(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    should_continue = True

    while should_continue:
        operation = str(input("Pick an operation: "))
        second_number = int(input("What's the second number? "))
        function_to_call = operations[operation]
        result = function_to_call(first_number, second_number)
        print(f"{ first_number } { operation } { second_number } = { result }")

        if input(f"Type 'y' to continue calculating with { result }, or type 'n' to start a new calculation: ") == 'y':
            first_number = result
        else:
            should_continue = False

calculator()