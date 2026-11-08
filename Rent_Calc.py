#--------------------------TIP CALCULATOR-------------------------------------#
print("Welcome to the tip Calculator!")
initial_bill=float(input("What was the total bill? $"))
tip=float(input("How much tip would you like to give? 10, 12, or 15?"))
people=float(input("How many people to split the bill?"))
tip_bil=((initial_bill*tip)/100)
last_bill=((tip_bil+initial_bill)/people)
print("Each person should pay: $" +str(last_bill))
