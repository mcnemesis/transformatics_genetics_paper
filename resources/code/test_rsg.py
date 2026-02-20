#!/usr/bin/env python3
###################################
# RSG: Random Sequence Generator
#----------------------------------
# A complete standalone reference
# implementation in Python 3.
# Copyright: Fut. Prof. JWL
# Nuchwezi Research (nuchwezi.com)
###################################

import time

##---[ FLSA(s,k) ]
def flsa(s, k0):
    n = len(s)
    if n < 2:
        return s,k0
    k = k0 % n
    k = 1 if k < 1 else k
    new_s = s
    while True:
        if k == n:
            break
        p_index = k
        p_start = 0
        sub_p_index = int(0.5 * p_index)
        sub_p_l = new_s[p_start:sub_p_index]
        sub_p_r = new_s[sub_p_index:p_index]
        rest_p = new_s[p_index:n]
        swapped = sub_p_r + sub_p_l
        if k%2 == 1:
            new_s = rest_p + swapped
        else:
            new_s = swapped + rest_p
        k += 1
    return new_s,k

#---[ SLSA(s,k) ]
def slsa(s, k0):
    n = len(s)
    if n < 2:
        return s,k0
    k = k0 % n
    k = 1 if k < 1 else k
    new_s = flsa(s,n-k)[0] #invoke FLSA with k0=n-k
    while True:
        if k == n:
            break
        p_index = k
        p_start = 0
        sub_p_index = int(0.5 * p_index)
        sub_p_l = new_s[p_start:sub_p_index]
        sub_p_r = new_s[sub_p_index:p_index]
        rest_p = new_s[p_index:n]
        swapped = sub_p_r + sub_p_l
        if k%2 == 1:
            new_s = rest_p + swapped
        else:
            new_s = swapped + rest_p
        k += 1
    return new_s,k


#---[ RNG(ll,ul) ]
def rng(l,u):
    lu = max(l,u)
    ll = min(l,u)
    lu = lu + 1 if ll == lu else lu
    part_k = int((lu - ll) * 0.5)
    candidates = flsa(list(range(ll,lu+1)),part_k)[0] #invokes FLSA
    n = len(candidates)
    pick = int(flsa(str(time.time()).replace('.',''),1)[0])%n #because we need an entropy source!
    return candidates[pick]

#---[ SHUFFLE(s) ]
def shuffle(s):
    n_s = len(s)
    if n_s < 2:
        return s
    random_k = rng(1,n_s)
    shuffled_s,k = slsa(s,random_k)
    random_k2 = rng(1,int(n_s*0.5))
    shuffled_s,k = flsa(shuffled_s,random_k2)
    return shuffled_s

#---[ USYMBOLSET(s) ]
def usymbolset(s):
    n_s = len(s)
    if n_s <= 1:
        return s
    resultant = []
    for i in range(n_s):
        s_i = s[i]
        if not (s_i in resultant):
            resultant.append(s_i)
    return resultant

#---[ PROTRACT(s,n) ]
def protract(s,n):
    n_s, n = len(s), int(n)
    if n_s < 1:
        return s
    if n < n_s:
        return s[:n]
    if n == n_s:
        return s
    multiple = int(n / n_s)
    target_n = n_s * multiple + 1
    resultant = s
    i = 1
    while i < target_n:
        resultant = resultant + s
        i += 1
    return resultant[:n] # could potentially, also compress

#---[ SHUFFLE(s) ]
def shuffle(s):
    n_s = len(s)
    if n_s < 2:
        return s
    random_k = rng(1,n_s)
    shuffled_s,k = slsa(s,random_k)
    random_k2 = rng(1,int(n_s*0.5))
    shuffled_s,k = flsa(shuffled_s,random_k2)
    return shuffled_s

#---[ SELECT(n,s) ]
def select(n,s):
    n_s, n = len(s), int(n)
    resultant = []
    if n <= 0:
        return resultant
    n = n if n <= n_s else n_s
    resultant = s[:n]
    return resultant

#---[ RSG(n,s) ]
def rsg(n,s, DEBUG=False):
    n_s,n = len(s),int(n)
    resultant = []
    if n == 0 or n_s == 0:
        return resultant
    # first, compute the u-symbol set
    if DEBUG:
        print(f'input sequence: {s}')
    s_usymbolset = usymbolset(s)
    if DEBUG:
        print(f"u-symbolset: {s_usymbolset}")
    n_us = len(s_usymbolset)
    # then chain the sequence transformers...
    resultant = shuffle(s_usymbolset) # randomize the symbol set
    if DEBUG:
        print(f"shuffled u-symbolset: {resultant}")
    resultant = protract(resultant,n*2*n_us)
    if DEBUG:
        print(f"protracted: {resultant}")
    resultant = shuffle(resultant)
    if DEBUG:
        print(f"shuffled: {resultant}")
    # then pick only as much as was asked for...
    resultant = select(n,resultant)
    if DEBUG:
        print(f"selection:{n}: {resultant}")
    return resultant

#---[ TEST RSG ]
#s = [0,1,2,3,4,5,6,7,8,9,0,1]
#s = [0,1,2,3,4,5,6,7,8,9] --> rsg(0,s) --> [],
# rsg(1,s) --> [6], [1], [0], etc.
# rsg(3,s) --> [2, 9, 5], [0, 1, 2],[5, 6, 5], etc.
#s = ['A' , 'C' , 'G' , 'T' , 'U']
# rsg(1,s) --> ['T'], ['A'], ['G'], etc.
s = ['A' , 'T' , 'C' , 'G']
# rsg(3,s) --> ['C', 'G', 'A'], ['G', 'T', 'C'] # random DNA codons!
#s = list('abcdefghijklmnopqrstuvwxyz')
#result = rsg(3,s,False)
#print(f"RSG result: {result}")

#print(f"10 random DNA codons via RSG(3,['A,'C','T','G']):\n\n{[str(''.join(rsg(3,s,False))) for i in range(1,11)]}")

# what of generating sentences from words?
# e.g pass in a glossary
print('\n'.join([' '.join(rsg(10,['CAT','DOG','PEN','ACE','SKY','EYE','IS','THAT','NO','YOU'])) for i in range(1,6)]))
# --> ['YOU', 'IS', 'NO', 'DOG', 'SKY', 'THAT', 'ACE', 'EYE', 'CAT', 'PEN']
