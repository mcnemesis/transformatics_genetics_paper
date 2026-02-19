#!/usr/bin/env python3
import math

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
    return new_s,k

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
    return new_s,k


#TEST:
#s,k = [0,1,2,3,4,5,6,7,8,9],8
#rs=slsa(s,k)
#print(f"For s={s} and k={k}:\ns*={rs}") # show test results
