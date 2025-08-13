#!/usr/bin/env python3
#print(f"k={k} | s[{p_start}:{p_end}] | sub_part_end:{sub_p_end} | {new_s[p_start]} -> {new_s[p_end]} | sub_l = {sub_p_l} | sub_r = {sub_p_r} | swapped = {sub_p_r + sub_p_l} | rest:{rest_p}\r\nnew_s:{new_s}\r\n\r\n")
import random as rng
import math
#s = ['a','b','c','d','e','f','g','h']
s = [0,1,2,3,4,5,6,7,8,9]
N = len(s)
k = rng.randint(0,N)
def shuffler_a(s, k):
    #print(f"\r\n---||START SHUFFLER-A: with s={s} | k={k}\r\n")
    n = len(s)
    start_k = k
    new_s = s
    i = 0
    while i < n:
        p_index = k % n
        p_start = 0
        p_end = p_index * 2
        sub_p_end = p_index
        if (k * 2) > n:
            #print(f"Shuffler-A Seq: AT k={start_k}")
            break

        sub_p_end = math.ceil(p_end * 0.5)
        sub_p_l = new_s[p_start:sub_p_end]
        sub_p_r = new_s[sub_p_end:p_end]
        rest_p = new_s[k*2:n]
        swapped = sub_p_r + sub_p_l
        new_s = swapped + rest_p
        #print(f"{k}-gram | sub_l = {sub_p_l} | sub_r = {sub_p_r} | swapped = {sub_p_r + sub_p_l} | rest:{rest_p}\r\nnew_s:{new_s}\r\n\r\n")
        k += 1
        #input()
    return new_s,k


def shuffler_b(s, k):
    new_s_a,last_k_a = shuffler_a(s,k)
    #print(f"\r\n---||START SHUFFLER-B: with s={s} | k={k}\r\n")
    print(f"\r\nk={k} | s={s}\r\n")
    s = new_s_a
    k = last_k_a
    n = len(s)
    start_k = k
    new_s = s
    i = 0
    while i < n:
        p_index = k % n
        p_start = 0
        p_end = p_index * 2
        sub_p_end = p_index
        if k == n:
            #print(f"Shuffler-B Seq: for k={start_k}")
            #print(f"k={start_k}")
            break

        sub_p_end = math.ceil(p_end * 0.5)
        sub_p_l = new_s[p_start:sub_p_end]
        sub_p_r = new_s[sub_p_end:p_end]
        rest_p = new_s[k*2:n]
        swapped = sub_p_r + sub_p_l
        new_s = swapped + rest_p
        #print(f"{k}-gram | sub_l = {sub_p_l} | sub_r = {sub_p_r} | swapped = {sub_p_r + sub_p_l} | rest:{rest_p}\r\nnew_s:{new_s}\r\n\r\n")
        k += 1
        #input()
    return new_s,k

#new_s_a,last_k_a = shuffler_a(s,k)
#print(new_s_a)
#new_s_b,last_k_b = shuffler_b(new_s_a,last_k_a)
#print(new_s_b)

s_k = 0
while s_k < k:
    new_s_b,last_k_b = shuffler_b(s,s_k)
    s = new_s_b
    k = last_k_b
    s_k += 1
    #print(new_s_b)
