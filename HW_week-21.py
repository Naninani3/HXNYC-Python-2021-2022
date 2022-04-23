'''
Write a function to calculate the sum of all the elements with even index (or odd index, you made the call. 😎) 
'''
 
def sum_list(li, oddeven):

    sum=0

    if oddeven=="even":

        for n in li[::2]:

            sum=sum+n

    else:

        for n in li[1::2]:

            sum=sum+n

    return sum

 

li=[1,2,3,34,4,5,6,7]

print(f"The odd sum of the list is {sum_list(li, 'odd')}")

print(f"The even sum of the list is {sum_list(li, 'even')}")


 
