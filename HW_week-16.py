'''
write a function to print a string BACKWARD.
'''
def backwards(string):

    revstr = ''

    for i in string:

        revstr = i + revstr

    return revstr

 

string = "Alex"

print("Original string: ",string)

print("backswards string: ",backwards(string))
