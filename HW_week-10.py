'''
Please work on logical operations and be familiar with the conditional statement's syntax. 

Please write a function to print the corresponding sentences:
1) If raining and if "I have  umbrella ", print('bring my umbrella!')
2) If it rains but I do not have an umbrella, print ("bad luck !)
3) if I have an umbrella, but it doesn't rain, print("no worries")
'''

This is the Fibonacci sequence


import math

def F(n):

    if n>=0:

        if n==0:

            return 0

        elif n==1:

            return 1

        else:

            return F(n-1)+F(n-2)

    else:

        return math.nan
