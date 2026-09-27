Starting_POP = float (input("How many are there?"))
Rate = int(input("What is the rate of growth?"))
Untill_Rate = float(input("How long does it take to acheieve this rate?"))
Future = int(input("How long for the simulation to last?"))

Periods = int(Future / Untill_Rate)
for i in range (Periods):
    Starting_POP = Starting_POP * Rate


    
print("The predicted population is", Starting_POP)

