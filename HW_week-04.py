'''
Based on your previous homework, write a unit-converter function. 
(hint, I would like you practice the syntax to define a function)
'''

def repeat(random_sentence) :
    print (random_sentence)
    print (random_sentence)

random_sentence= 'I love python'
repeat (random_sentence)

Length= 3
Width= 8
Area= Length*Width
print('Area is', Area)

def area() :
    Length= 3
    Width= 8
    Area= Length*Width
    print('Area is', Area)

area()



def pound_to_kilo():
    abc=input('how many pounds do you want to convert into kilograms? ')
    abc_int=int(abc)
    xyz=abc_int/2.2046
    xyz=round(xyz, 2)
    print(abc+ ' pounds = ' +str(xyz)+ ' kilograms')
    

pound_to_kilo()

def lb_to_kilo(pound):
    kg=pound/2.2046
    #kg=round(kg, 2)
    return round(kg, 2) 
    

lb_to_kilo(333)

def min_to_sec(minute):
    second=minute*60
    return round(second, 2)
   

sec=min_to_sec(3.3)
print("the number of seconds= " + str(sec))


