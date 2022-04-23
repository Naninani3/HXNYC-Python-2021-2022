'''
If you haven't finished your Lab (loop and count: count how many times a letter appears in a string), please finish offline. 
Please WRITE A FUNCTION (include the arguments).
'''

def countletter(string,letter):

    count=0

    for l in string:

        if l==letter:

            count = count + 1

    return count
