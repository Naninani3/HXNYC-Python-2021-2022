***
taking a value and finding more keys --> Returns a list of keys with the finding value.
e.g. : crakers={'A':5, 'B':3, 'C':1,'D':3} --> Return ['B','D']
***

def reverselookup(d,v):
    l=[]
    for i in d.keys():
        if d[i]==v:
            l.append(i)
    return l
        
crackers={'A':5, 'B':3, 'C':1,'D':3}
reverselookup(crackers, 3)
