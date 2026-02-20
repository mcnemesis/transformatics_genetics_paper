#!/usr/bin/env python3

#---[ SELECT(n,s) ]
def select(n,s):
    n_s, n = len(s), int(n)
    resultant = []
    if n <= 0:
        return resultant
    n = n if n <= n_s else n_s
    resultant = s[:n]
    return resultant

#---[ TEST SELECT ]
s = [0,1,2,3,4,5,6,7,8,9]
#s = [0,1,2,3,4,5,6,7,8,9] --> select(2,s) --> [0,1],
# select(12,s) --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], etc.
#s = ['A' , 'C' , 'G' , 'T' , 'U']
# s = ['A' , 'C' , 'G' , 'T' , 'U'] --> select(3,s) --> ['A', 'C', 'G'], etc.
result = select(15.3,s)
print(result)
