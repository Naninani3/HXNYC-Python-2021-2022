'''
write a code (and stack diagram) for Fibonacci numbers.==> Please digest it and learn how the recursion happens
'''
 

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

 
