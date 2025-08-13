#!/usr/bin/env python3
import random as rng
import math

def lu_shuffler_a(s, k):
    #print(f"k={k} | s={s}")
    n = len(s)
    new_s = s
    while True:
        if (k * 2) > n:
            break
        p_index = k % n
        p_start = 0
        p_end = p_index * 2
        sub_p_end = math.ceil(p_end * 0.5)
        sub_p_l = new_s[p_start:sub_p_end]
        sub_p_r = new_s[sub_p_end:p_end]
        rest_p = new_s[k*2:n]
        swapped = sub_p_r + sub_p_l
        new_s = swapped + rest_p
        k += 1
    return new_s,k


def lu_shuffler_b(s, k):
    print(f"k={k} | s={s}")
    n = len(s)
    new_s_a,last_k_a = lu_shuffler_a(s,n-k)
    s = new_s_a
    k = last_k_a
    new_s = s
    while True:
        if k == n:
            break
        p_index = k % n
        p_start = 0
        p_end = p_index * 2
        sub_p_end = math.ceil(p_end * 0.5)
        sub_p_l = new_s[p_start:sub_p_end]
        sub_p_r = new_s[sub_p_end:p_end]
        rest_p = new_s[k*2:n]
        swapped = sub_p_r + sub_p_l
        new_s = swapped + rest_p
        k += 1
    return new_s,k


#s = [0,1,2,3,4,5,6,7,8,9] # base-10 n-SSI
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'A' , 'C' , 'G' , 'T' , 'U'] #na-SS+na-SS
s = ['A' , 'C' , 'G' , 'T' , 'U' , 'U' , 'T' , 'G' , 'C' , 'A'] #na-SS+complement(na-SS)
N = len(s)
k = 20 #rng.randint(0,N)

s_k = 0
while s_k < N:
    new_s_b,last_k_b = lu_shuffler_b(s,s_k)
    s = new_s_b
    s_k += 1
