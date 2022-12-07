import os
os.system('cls')
bill = input("What was the total bill? $")
tipPerc = input("What percentage tip would you like to give? 10, 12 or 15? ")
people = input("How many people to split the bill? ")
calculate = (float(bill)+(float(bill)*float(tipPerc)/100))/int(people)
print(f"Each person should pay: ${round(calculate, 2)}")