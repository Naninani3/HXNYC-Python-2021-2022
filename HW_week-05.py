'''
Finish your Function to calculate the tip of your dinner. 
Please try to use 2 arguments (dinner cost and tip percentage) for that function.
'''

dinnercost=100
tippercentage=15%
tip=dinercost*tippercentage

DC=100
TP=0.15
Tip=DC*TP
print(Tip)

def tip_calculator(dinner_cost, tip_percentage):
    tip=dinner_cost*tip_percentage/100
    return tip

x=tip_calculator(100,10)
print(f"tip = ${x}")

tip_calculator(100,10)
print(f"tip = ${tip_calculator(100,10)}")
