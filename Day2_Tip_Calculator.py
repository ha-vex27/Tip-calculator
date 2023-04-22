

print("WELCOME TO THE  HARVEY'S TIP CALCULATOR")

bill= float(input("What is the total bill? GHc"))

tip= int(input("What percentage would you like to give? "))

people=int(input("How many people to split the bill? "))

total_bill=(tip/100*bill+bill)

print(f"New Bill with Tip: GHc{total_bill}")


pay= (total_bill/people)
print(f"Each person should pay: {pay}")