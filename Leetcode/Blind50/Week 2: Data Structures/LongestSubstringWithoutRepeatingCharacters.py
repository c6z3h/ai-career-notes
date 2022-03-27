class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        "dvdf"
        """
        
        l = 0
        n = len(s)
        charSet = set()
        res = 0
        
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, len(charSet))
            
        return res
