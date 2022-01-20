# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 08:34:30 2021

@author: Mu-Ping
"""

test = [[-2,1,-3,4,-1,2,1,-5,4], [-2,-1,2,3,-2,4], [-2,5,-4,1,2,4]]

class Solution(object):
    
    def maxSubArray(self, nums):
        ans = []
        subans = [nums[0]]
        
        l = len(nums)
        if l == 0: return 0
        res = curr = nums[0]
        
        for i in range(1, l):
            if curr < 0 or nums[i] > curr+nums[i]:
                subans = [nums[i]]
                curr = nums[i]
            else:
                subans.append(nums[i])
                curr += nums[i]
            
            if curr > res:
                ans = subans[:]
                res = curr
        
        print("\nTest:", nums)
        print("Maximum suarray sum:",res)
        print("Maximum suarray:", ans)
        
        return res

solution = Solution()
for i in test:
    res = solution.maxSubArray(i)
    

    