'''
Try to finish the searching function: search a particular character from a string, return True if a given character is found.Otherwise, return False.
Hint: think about the arguments: how many arguments?. how to make your function more generalized.  
'''

def isCharinString(char,string):

    for letter in string:

        if char==letter:

            return True

    return False

 
