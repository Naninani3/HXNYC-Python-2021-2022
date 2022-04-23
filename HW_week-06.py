'''
Finish the our lab in the class: calculate the distance by speed and time.
Please: 1. Use "return"
        2. make your code more interactive !
'''

import math

r=2
area=math.pi*2*2
print(area)

def distance_calculator():
    speed=input("What is your speed in miles per hour? ")
    time=input("How long have you traveled in hours? ")
    
    distance=float(speed)*float(time)
    print(f"You have traveled {distance} miles")
    return distance
distance_calculator()
