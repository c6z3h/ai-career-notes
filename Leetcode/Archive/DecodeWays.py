class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        
        REACTO: Repeat, Example, Algorithm, Code, Test, Optimize.
        Case 1: ABC
        AB C
        A BC
        A B C
        
        Case 2: ABCD (count = 5)
        AB CD
        AB C D
        A BC D
        A B CD
        A B C D
        """
#         count = 0
        
#         def dp(s, count):
#             if len(s)==2:
#                 if 1 <= int(s) <= 26:
#                     count += 1
#                 if int(s[0]) != 0:
#                     dp(s[1], count)
#             if len(s)>2:
#                 if int(s[0]) != 0:
#                     dp(s[1:], count)
#                 if int(s[0]) != 0 and 1 <= int(s[:1]) <= 26:
#                     # it is a valid two-digit
#                     dp(s[2:], count)
#             if len(s)==1 and int(s) != 0:
#                 count +=1
        
#         dp(s, count)
        
#         return count
        
        if not s:
            return 0
        
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        
        for i in range(1,n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if len(s[i-2:i])==2 and '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]
                
        return dp[n]
