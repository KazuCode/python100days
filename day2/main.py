print("Welcome to the Tip Calculator.")
bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
perticipants = int(input("How many people to split the bill? "))

equal_part = round((bill / perticipants) * (1 + (percentage/100)), 2)
print(f"Each person should pay: ${ equal_part }")