# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 21:51:37 2023

@author: Dongli
"""

def Prime_String(n):
    nums = [i for i in range(2, n+1)]
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
    combined_string = ''.join(str(num) for num in nums) 
    return combined_string
    
primes = Prime_String(20231)
