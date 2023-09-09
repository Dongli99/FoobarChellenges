# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 07:28:22 2023

@author: Dongli
"""
"""
Numbers Station Coded Messages==============================

When you went undercover in Commander Lambda's organization, you set up a coded messaging 
system with Bunny Headquarters to allow them to send you important mission updates. Now that 
you're here and promoted to Henchman, you need to make sure you can receive those messages -- 
but since you need to sneak them past Commander Lambda's spies, it won't be easy!Bunny HQ has 
secretly taken control of two of the galaxy's more obscure numbers stations, and will use them 
to broadcast lists of numbers. They've given you a numerical key, and their messages will be 
encrypted within the first sequence of numbers that adds up to that key within any given list 
of numbers. Given a non-empty list of positive integers l and a target positive integer t, 
write a function solution(l, t) which verifies if there is at least one consecutive sequence 
of positive integers within the list l (i.e. a contiguous sub-list) that can be summed up to 
the given target positive integer t (the key) and returns the lexicographically smallest list 
containing the smallest start and end indexes where this sequence can be found, or returns the 
array [-1, -1] in the case that there is no such sequence (to throw off Lambda's spies, not 
all number broadcasts will contain a coded message).For example, given the broadcast list l 
as [4, 3, 5, 7, 8] and the key t as 12, the function solution(l, t) would return the list 
[0, 2] because the list l contains the sub-list [4, 3, 5] starting at index 0 and ending at 
index 2, for which 4 + 3 + 5 = 12, even though there is a shorter sequence that happens later 
in the list (5 + 7). On the other hand, given the list l as [1, 2, 3, 4] and the key t as 15, 
the function solution(l, t) would return [-1, -1] because there is no sub-list of list l that 
can be summed up to the given target value t = 15.To help you identify the coded broadcasts, 
Bunny HQ has agreed to the following standards: 
    - Each list l will contain at least 1 element but never more than 100.
    - Each element of l will be between 1 and 100.
    - t will be a positive integer, not exceeding 250.
    - The first element of the list l has index 0. 
    - For the list returned by solution(l, t), the start index must be equal or smaller than the end index. 
Remember, to throw off Lambda's spies, Bunny HQ might include more than one contiguous 
sublist of a number broadcast that can be summed up to the key. You know that the message 
will always be hidden in the first sublist that sums up to the key, so solution(l, t) should 
only return that sublist.
"""
def solution(l, t):
    res = l
    for i in range(len(l)-1):
        s = l[i]
        tmp = [i]
        
        if s == t:
            res = [i]
            return res
        elif s > t:
            continue
        
        if i <= len(l)-2:
            j = i + 1            
        else:
            continue
        
        while s < t:
            s += l[j]
            if s <= t:
                tmp.append(j)
            else:
                break
            if s == t and len(tmp) < len(res):
                res = tmp
                break
            if j <= len(l)-2:
                j += 1
        
    if len(res) == len(l):
        return [-1, -1]
    else:
        return [res[0], res[-1]]
    
result = solution([4, 3, 10, 2, 8], 17)
print(result)
    