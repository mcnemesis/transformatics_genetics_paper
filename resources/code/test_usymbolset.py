#!/usr/bin/env python3

#---[ USYMBOLSET(s) ]
def usymbolset(s):
    n_s = len(s)
    if n_s <= 1:
        return s

    # the next commented-out code would kinda work,
    # if we just wanted a dirty and pythonic solution, but
    # it doesn't respect order of first occurrence!
    #resultant = list(set(s))

    #our CORRECT solution for unspecific symbol set..
    resultant = []
    for i in range(n_s):
        s_i = s[i]
        if not (s_i in resultant):
            resultant.append(s_i)
    return resultant

#---[ TEST USYMBOLSET ]
#s = [0,1,2,3,4,5,6,7,8,9]
#s = [0,1,2,3,4,5,6,7,8,9] #--> usymbolset(s+s+s+s)
#result = usymbolset(s+s+s+s)
#--> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#s = [1,0,1,1,1,1,1,0,1,1] #--> usymbolset(s) --> [0,1]
#s = "3.1415926535898" # --> usymbolset(s) -->
#['3', '.', '1', '4', '5', '9', '2', '6', '8']
s = ['A' , 'C' , 'G' , 'T' , 'U' , 'U' , 'T' , 'G' , 'C' , 'A'] #w/duplication
# usymbolset(s) --> ['A', 'C', 'G', 'T', 'U']
result = usymbolset(s)
print(result)
