class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # trivial situation
        if len(s) <= 1: return s
        
        # Dynamic Programming table
        length = len(s)
        dp = [[False]*length for _ in range(length)]
        
        longest = 0
        start = 0
        end = 0
        
        # Complete the DP table
        for j in range(0, length):
            for i in range(0, j+1):

                # base case1
                if(i==j):
                    dp[i][j] = True
                    
                # base case2    
                elif(i==j-1 and s[i]==s[j]):
                    dp[i][j] = True
                
                # otherwise
                else:    
                    dp[i][j] = (dp[i+1][j-1] and s[i]==s[j])
                    
                if dp[i][j] and longest <= j-i+1:
                    longest = j-i+1
                    start = i
                    end = j+1
                    
        return s[start:end]

