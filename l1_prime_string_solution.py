# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:51:37 2023

@author: Dongli
"""
def Solution(i):
    # filter prime number with Sieve of Eratosthenes
    nums = [i for i in range(2, 20232)]
    i = 0
    while i < len(nums):
        f = nums[i]
        j = i+1
        while j < len(nums):
            if nums[j] % f == 0:
                nums.pop(j)
            else:
                j+=1
        i+=1
    prime_string = ''.join(str(num) for num in nums)
    
    # find code for i
    return prime_string[i, i+5]

    
    
    
