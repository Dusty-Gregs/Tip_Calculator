#tip calculator
print("Welcome to the tip calculator!")
bill_total = float(input("What was the total bill? $"))
tip_percent = int(input("How much tip would you like to give? 15, 18, or 20? "))
party_size = int(input("How many people to split the bill? "))

calculation = round(bill_total * (1 + tip_percent / 100) / party_size, 2)

calculation_two_decimal = format(calculation, '.2f')

print(f"Each person should pay: ${calculation_two_decimal}")