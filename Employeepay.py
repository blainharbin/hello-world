Regular_Hours = float(input("How many regular hours did you work?"))

Wage = float(input("How much is your hourly wage?"))

Overtime_Hours = float (input("How many overtime hours did you work?"))

Regular_Pay = Regular_Hours * Wage
Overtime_Pay = Overtime_Hours * Wage * 1.5

Final_Pay = Regular_Pay + Overtime_Pay
print ("Your Total pay for the week is:", str(Final_Pay))



