class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        chars = [0]*128 # English letters, digits, symbols and spaces
        
        left = right = 0 # default two index
        ans = 0
        
        for right in range(len(s)):
            
            if chars[ord(s[right])] == 1:
                while s[left]!=s[right]:
                    chars[ord(s[left])] = 0
                    left += 1
                left += 1
                
            else:
                chars[ord(s[right])] = 1
                
            ans = max (ans, right-left+1)
                
        return ans