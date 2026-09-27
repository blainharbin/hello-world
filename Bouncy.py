

Height = int(input("How high was the ball dropped from?"))
Bounces = int(input("How many times did the ball bounce?"))
bouncinessindex = float(input("What is the bounciness index of the ball?"))
Total = 0

for i in range(Bounces):
    Bounce = Height * bouncinessindex
    Total = Bounce + Height + Total
    Height = Bounce
    Distance = Total
    
    
     

print("The distance the ball travled is", Distance)
    
    
