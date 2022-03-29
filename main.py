print("Welcome to the Tip Calculator.\n")

bill = input("What was the total bill? ")
percentage = input("What percentage of a tip would you like to give? 10 , 12, 15, 20 etc? \n")

people = input("How many people are spitting this bill? \n")
actual_percentage = float(percentage)
actual_percentage /= 100


tip = round(float(bill) * float(actual_percentage), 2)

print(f"Your caclulated tip is ${tip}.\n")


result = (float(tip) + float(bill)) / float(people)
total = round(result, 2)
total = "{:.2f}".format(result)
print(f"Each person should pay ${total}.")
