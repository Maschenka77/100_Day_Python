#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

print("Welcome to the tip calculator!")
total_bill = float(input("What is the total bill? "))

percent = int(input("What percentage tip would you like to give? "))
percent_div = percent/100

split = int(input("How many people to split the bill? "))

bill_splitted = total_bill/split
with_tip = round(bill_splitted*(1+percent_div),2)

print(f"Each person should pay: ${with_tip}")
