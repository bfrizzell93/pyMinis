print("Welcome to the tip calculator.")
total = float(input("What was the total bill? $"))

people = int(input("How many people to split the bill?"))

tip = int(input("What percentage tip would you like to give?"))

tippercent = tip / 100 

total_tip_amount = total * tippercent

total_bill= total + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")