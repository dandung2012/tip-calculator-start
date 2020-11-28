#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

#greet
print("Welcome to the tip calculator.\n")


total_bill = input("What was the total bill?\n")
tip = input("What precentage tip would you like to give?\n")
after_tip = int(total_bill)*(int(tip)/100+1)

split_bill = input("How many people to split the bill?\n")
bill = int(after_tip)/int(split_bill)

actual_bill = round(bill,3)
print(f"each person should pay:{actual_bill}")
