'''
Traverse a list (all the items are numbers), write a function to calculate the sum of the list.
'''

def sumList(numList):

    sum=0

    for n in numList:

        sum=sum+n

    return sum

 

sumList([1,2,3])
