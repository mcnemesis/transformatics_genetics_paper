#!/usr/bin/env python3
#|------------------------------------------|
# The Lu-Shuffle Algorithms: FLSA, SLSA
# And the Random Sequenge Generator: RSG
#---[copyright: Joseph Willrich Lutalo
# jwl@nuchwezi.com | code first made public
# in the book
# "Applying TRANSFORMATICS in GENETICS" 2025
# REF:____ (to come soon)
#|------------------------------------------|
import math
import time

def lu_shuffler_a(s, k0):
    n = len(s)
    if n < 2:
        return s,k0 #essentially, nothing to shuffle
    # make k meaningful...
    k = k0 % n
    k1 = k # for tracing/debugging...
    k = 1 if k < 1 else k # can't partition between nothing
    new_s = s
    while True:
        if k == n: #can't partition between nothing
            break
        p_index = k
        p_start = 0
        sub_p_index = math.ceil(0.5 * p_index)
        #print(f"At k={k} |"
        #        +f" [[{p_start}-{sub_p_index}][{sub_p_index}-"
        #        +f"{p_index}][{p_index}-{n}]")
        sub_p_l = new_s[p_start:sub_p_index]
        sub_p_r = new_s[sub_p_index:p_index]
        rest_p = new_s[p_index:n]
        swapped = sub_p_r + sub_p_l # first swap
        if k%2 == 1: # k is odd
            new_s = rest_p + swapped # second swap
            #print(f"At k={k} s -->"
            #+f"[{p_index}-{n}][{sub_p_index}-"
            #+f"{p_index}][{p_start}-{sub_p_index}] == {new_s}")
        else:
            new_s = swapped + rest_p # soft swap
            #print(f"At k={k} s --> [{sub_p_index}-"
            #        +f"{p_index}][{p_start}-"
            #        +f"{sub_p_index}][{p_index}-{n}] == {new_s}")
        k += 1 # so we advance from k-gram to (k+1)-grams
    #print(f"k={k1} | s={new_s}")
    return new_s,k


def lu_shuffler_b(s, k0):
    n = len(s)
    if n < 2:
        return s,k0
    k = k0 % n
    k1 = k
    k = 1 if k < 1 else k
    new_s = lu_shuffler_a(s,n-k)[0] #invoke FLSA with k0=n-k
    while True:
        if k == n:
            break
        p_index = k
        p_start = 0
        sub_p_index = math.ceil(0.5 * p_index)
        sub_p_l = new_s[p_start:sub_p_index]
        sub_p_r = new_s[sub_p_index:p_index]
        rest_p = new_s[p_index:n]
        swapped = sub_p_r + sub_p_l
        if k%2 == 1:
            new_s = rest_p + swapped
        else:
            new_s = swapped + rest_p
        k += 1
    #print(f"k={k1} | s={new_s}")
    return new_s,k


#---[ USYMBOLSET(s) ]
def usymbolset(s):
    n_s = len(s)
    if n_s <= 1:
        return s
    # the next code would kinda work, except it doesn't respect order of first occurrence!
    #resultant = list(set(s))
    resultant = []
    for i in range(n_s):
        s_i = s[i]
        if not (s_i in resultant):
            resultant.append(s_i)
    return resultant

#---[ TEST USYMBOLSET ]
#s = [0,1,2,3,4,5,6,7,8,9]
# s = [0,1,2,3,4,5,6,7,8,9] --> usymbolset(s+s+s+s) --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#s = [1,0,1,1,1,1,1,0,1,1] --> usymbolset(s) --> [0,1]
#s = "3.1415926535898" # --> usymbolset(s) --> ['3', '.', '1', '4', '5', '9', '2', '6', '8']
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'U' , 'T' , 'G' , 'C' , 'A'] #na-SS+complement(na-SS)
# usymbolset(s) --> ['A', 'C', 'G', 'T', 'U']
#result = usymbolset(s)
#print(result)

#---[ PROTRACT(s,n) ]
def protract(s,n):
    n_s = len(s)
    if n_s < 1:
        return s
    if n < n_s:
        return s[:n]
    if n == n_s:
        return s
    multiple = math.ceil(n_s / n)
    target_n = n * multiple
    resultant = s
    i = 1
    while i < target_n:
        resultant = resultant + s
        i += 1
    return resultant[:n]




#---[ Examples Follow ]
#s = [0,1,2,3,4,5,6,7,8,9] # base-10 n-SSI
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'A' , 'C' , 'G' , 'T' , 'U'] #na-SS+na-SS
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'U' , 'T' , 'G' , 'C' , 'A'] #na-SS+complement(na-SS)
#N = len(s)
#k = 20 #random_ng(0,N)
#result,k = lu_shuffler_b(s,k)

#---[ TEST PROTRACT ]
# s = [0,1,2,3,4,5,6,7,8,9], n = 3 --> [0,1,2]
# s = [0,1,2,3,4,5,6,7,8,9], n = 23 -->
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
#result = protract(s,23)
#print(result)


#---[ RNG(ll,ul) ]
def random_ng(l,u):
    lu = max(l,u)
    ll = min(l,u)
    lu = lu + 1 if ll == lu else lu
    part_k = 1
    candidates = lu_shuffler_a(list(range(ll,lu+1)),part_k)[0]
    n = len(candidates)
    pick = int(time.time())%n
    return candidates[pick]

#---[ TEST RNG ]
#for r in [[0,10],[0,1],[0,100],[1900,1999]]:
#    print(f"RNG From {r[0]}-{r[1]} -> {random_ng(r[0],r[1])}")


#---[ SHUFFLE(s) ]
def shuffle(s):
    n_s = len(s)
    if n_s < 2:
        return s
    random_k = random_ng(1,n_s)
    shuffled_s,k = lu_shuffler_b(s,random_k)
    random_k2 = random_ng(1,n_s)
    shuffled_s,k = lu_shuffler_a(shuffled_s,random_k2)
    return shuffled_s

#---[ TEST SHUFFLE ]
s = [0,1,2,3,4,5,6,7,8,9]
#s = [1,2,3,4]
# s = [0,1,2,3,4,5,6,7,8,9] --> [9, 3, 4, 7, 0, 5, 2, 1, 6, 8], [4, 5, 2, 8, 9, 3, 1, 6, 7, 0], etc.
#s = ['A' , 'C' , 'G' , 'T' , 'U']
# s = ['A' , 'C' , 'G' , 'T' , 'U'] --> ['C', 'G', 'T', 'U', 'A'], ['U', 'G', 'T', 'C', 'A'], etc.
#result = shuffle(s)
#print(result)

#---[ SELECT(n,s) ]
def select(n,s):
    n_s = len(s)
    resultant = []
    if n == 0:
        return resultant
    n = n if n <= n_s else n_s
    resultant = s[:n]
    return resultant

#---[ TEST SELECT ]
#s = [0,1,2,3,4,5,6,7,8,9]
#s = [0,1,2,3,4,5,6,7,8,9] --> select(2,s) --> [0,1], select(12,s) --> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], etc.
#s = ['A' , 'C' , 'G' , 'T' , 'U']
# s = ['A' , 'C' , 'G' , 'T' , 'U'] --> select(3,s) --> ['A', 'C', 'G'], etc.
#result = select(12,s)
#print(result)


#---[ RSG(n,s) ]
def rsg(n,s):
    n_s = len(s)
    resultant = []
    if n == 0 or n_s == 0:
        return resultant
    # first, compute the u-symbol set
    s_usymbolset = usymbolset(s)
    n_us = len(s_usymbolset)
    # then chain the transformers...
    resultant = shuffle(s_usymbolset) # randomize the symbol set
    resultant = protract(resultant,n*2*n_us)
    resultant = shuffle(resultant)
    # then pick only as much as was asked for...
    resultant = select(n,resultant)
    return resultant

#---[ TEST RSG ]
#s = [0,1,2,3,4,5,6,7,8,9]
#s = [0,1,2,3,4,5,6,7,8,9] --> rsg(0,s) --> [],
# rsg(1,s) --> [6], [1], [0], etc.
# rsg(3,s) --> [2, 9, 5], [0, 1, 2],[5, 6, 5], etc.
#s = ['A' , 'C' , 'G' , 'T' , 'U']
# rsg(1,s) --> ['T'], ['A'], ['G'], etc.
#s = ['A' , 'T' , 'C' , 'G']
#print(rsg(3,s) #--> ['C', 'G', 'A'], ['G', 'T', 'C'] # random DNA codons!
#result = str(select(8,s))
#result = ''.join(str(c) for c in rsg(150,['A','T','C','G']))
#result = rsg(10,['CAT','DOG','PEN','ACE','SKY','EYE','IS','THAT','NO','YOU'])
#result = random_ng(200,200)
#result = rsg(10,s)
#print(result)
#N=3*200; print(''.join(str(c) for c in rsg(N,['A','T','C','G'])));

#---[Some Further Experiments]
#s = [1,2,3,4]
#s = [1,2,3]
#s = [1,2]
#s = [0,1,2,3,4,5,6,7,8,9]
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'A' , 'C' , 'G' , 'T' , 'U'] #na-SS+na-SS
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'U' , 'T' , 'G' , 'C' , 'A'] #na-SS+complement(na-SS)

#---[Generate Lu-Shuffle Look-Up Tables]
#k = len(s)
#s_k = 0
#print(f"GIVEN s={s}")
#while s_k < k:
#    #lu_shuffler_a(s,s_k) # for FLSA
#    lu_shuffler_b(s,s_k)  # for SLSA
#    s_k += 1
