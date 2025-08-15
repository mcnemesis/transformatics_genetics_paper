#!/usr/bin/env python3
import math

def lu_shuffler_a(s, k):
    n = len(s)
    if n < 2:
        return s,k #essentially, nothing to shuffle
    # make k meaningful...
    k = k % n
    k_1 = k # for tracing/debugging...
    k = math.ceil(0.5*n) if 2*k > n else k # we partition into 2 equal halves
    k = 1 if k < 1 else k # can't partition between nothing
    new_s = s
    while True:
        if (k * 2) > n:
            break
        p_index = k
        p_start = 0
        p_end = 2 * p_index
        sub_p_end = math.ceil(0.5 * p_end)
        sub_p_l = new_s[p_start:sub_p_end]
        sub_p_r = new_s[sub_p_end:p_end]
        rest_p = new_s[2*k:n]
        swapped = sub_p_r + sub_p_l
        new_s = swapped + rest_p
        k += 1 # so we advance from k-gram to (k+1)-grams
    print(f"k={k_1} | s={new_s}")
    return new_s,k

#---[ Uncomment Lines Below to Run Examples ]
#---[Some Further Experiments]
s = [0,1,2,3,4,5,6,7,8,9]
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'A' , 'C' , 'G' , 'T' , 'U'] #na-SS+na-SS
#s = ['A' , 'C' , 'G' , 'T' , 'U' , 'U' , 'T' , 'G' , 'C' , 'A'] #na-SS+complement(na-SS)
#---[Generate Lu-Shuffle Look-Up Tables]
k = len(s)
s_k = 0
print(f"GIVEN s={s}")
while s_k < k:
    new_s_b,last_k_b = lu_shuffler_a(s,s_k) # for FLSA
    s_k += 1
