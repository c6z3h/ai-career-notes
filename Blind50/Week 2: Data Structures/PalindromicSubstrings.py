class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        # 1. Deal with odd-palindromes
        for i in range(len(s)):
            res += 1
            l,r=i,i
            while l>0 and r<len(s)-1 and s[l] == s[r]:
                l -= 1
                r += 1
                if s[l] == s[r]:
                    res += 1
        
        # 2. Deal with even-palindromes
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                res += 1
                l,r = i,i+1
                
                while l>0 and r<len(s)-1 and s[l] == s[r]:
                    l -= 1
                    r += 1
                    if s[l] == s[r]:
                        res += 1
        
        return res
