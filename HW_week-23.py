'''
Exercise 10.9 (Think Python). Write a function called remove_duplicates that takes a list and returns a new list with only the unique elements from the original. 
Hint: they don’t have to be in the same order  . (Please do not change the original list)
'''

def remove_duplicate(li):

    new=li.copy()

    new.sort()

    for i in reversed(range(1,len(new))):

        if new[i-1] == new[i]:

            new.pop(i-1)

    return new

 

print(remove_duplicate([2,2,3,43,5,6,7,5,4,23,4,5]))
