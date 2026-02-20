#!/usr/bin/env python3

import time

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

#FLSA
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

#SLSA
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

#---[ TEST SHUFFLE ]
s = [0,1,2,3,4,5,6,7,8,9]
# s = [0,1,2,3,4,5,6,7,8,9] --> [9, 3, 4, 7, 0, 5, 2, 1, 6, 8],
# [4, 6, 0, 3, 5, 2, 7, 9, 1, 8], etc.
#s = ['A' , 'C' , 'G' , 'T' , 'U']
# s = ['A' , 'C' , 'G' , 'T' , 'U'] --> ['C', 'G', 'T', 'U', 'A'],
# ['U', 'G', 'T', 'C', 'A'], etc.
result = shuffle(s)
print(result)


