class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_tb={}                      #用dict模擬 hash 參考

        for i in range(len(nums)):      #Ave：O(n)
            diff=target-nums[i]         #計算與答案的差 
            if(diff in hash_tb):        #Ave：O(1)
                return [hash_tb[diff], i]
            else:
                hash_tb[nums[i]]=i      #Ave：O(1)
