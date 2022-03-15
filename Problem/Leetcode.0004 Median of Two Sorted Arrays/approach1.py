class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1 = len(nums1)
        len2 = len(nums2)
        
        if len1 > len2: # choose the shorter to do
            
            return self.findMedianSortedArrays(nums2, nums1)
        
        start = 0
        end = len1
        realmidinmergedarray  = (len1 + len2 + 1) // 2
        
        while(start <= end):
            cut1 = (start + end) // 2
            cut2 = realmidinmergedarray - cut1
            l1 = float('-inf') if cut1==0 else nums1[cut1-1]
            r1 = float('inf') if cut1==len1 else nums1[cut1]
            l2 = float('-inf') if cut2==0 else nums2[cut2-1]
            r2 = float('inf') if cut2==len2 else nums2[cut2]
            
            if(l1 > r2):
                end = cut1 - 1
            elif(l2 > r1):
                start = cut1 + 1
            else:
                if ((len1 + len2) % 2 == 0):
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                return max(l1, l2)
