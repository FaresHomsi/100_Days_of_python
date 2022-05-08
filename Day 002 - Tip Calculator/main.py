print("Welcome to the Tip Calculator!")

bill = float(input ("What was the total bill? $ "))

precentage = float(input ("What precentage tip would you like to give? 10 , 12 , 15 ? " )) / 100

people_num = float(input ("How many people to split the bill? "))

tip = (bill * precentage )

result = round((bill + tip) / people_num, 2)

result ="{:.2f}".format(result)

message = (f"Each person should pay: $ {result}")

print(message)
