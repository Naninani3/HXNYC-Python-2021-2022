'''
We have 4 students in the class for the party, who are A,B,C,D. They bring 3,5,7,2 packs of crackers. Please 
1. create a dictionary with that information.
2. What is the key and what is the value?
3. Loop the dictionary and print all the keys and values.
'''

A='Alex'

B='Brandon'

C='Colin'

D='Declan'

cr={A:3,B:5,C:7,D:2}

key=cr.keys()

print(key)

value=cr.values()

print(value)

for k,v in cr.items():

    print(k,v)
