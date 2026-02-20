#!/usr/bin/env python3

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

#---[ TEST PROTRACT ]
s = [0,1,2,3,4,5,6,7,8,9]
n = 23 #--> [0,1,2]
# s = [0,1,2,3,4,5,6,7,8,9], n = 23 -->
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]
result = protract(s,n)
print(result)
