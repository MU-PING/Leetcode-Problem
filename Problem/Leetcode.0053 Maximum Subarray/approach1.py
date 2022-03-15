class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l = len(nums)
        if l == 0: return 0
        res = curr = nums[0]
        
        for i in range(1, l):
            if curr < 0 or nums[i] > curr+nums[i]:
                curr = nums[i]
            else:
                curr += nums[i]
            
            if curr > res:
                res = curr
        
        return res
