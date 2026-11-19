print("welcome to the tip calculator")
bill = float(input("what was the total bill?"))
tip = int(input("what percentage of tip u want to give to the people 10 15 20"))
people = int(input("how much people u want to spilt the bill into "))
bill_with_tip= tip / 100*bill + bill
print(bill_with_tip)