class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        # Recursive?
        
        if len(s) == 1, return s[0]
        if len(s) == 2,
            if s[0]==s[1]:
                return s
            else:
                return s[0]
        if len(s) == 3:
            if s[0] == s[2]:
                return s
            else:
                check for len(s) == 2
        
        """
        """
        # create a reference list. If value == 1, char is included in palindrome.
        palindrome_index = [0]*len(s)
        
        # 
        if len(s)==1:
            return s
        for i in range(len(s)):
            if s[i] == s[i+1]:
                if s[i-1] == s[i+2]:
                    return s[i-1:i+3]
                else:
                    return s[i:i+2]
            elif s[i] == s[i+2]:
                if s[i-1] == s[i+3]:
                    return s[i-1:i+4]
                else:
                    return s[i:i+3]
       """
        n = len(s)
        L = [[0]*len(s)]*len(s)
        
        for i in range(n):
            L[i][i] = 1
        # babad
        # 01234
        for cl in range(2, n+1):
            for i in range(n-cl+1):
                j = i+cl-1
                if s[i] == s[j] and cl == 2:
                    L[i][j] == 2
                elif s[i] == s[j]:
                    L[i][j] = L[i+1][j-1] + 2
                else:
                    L[i][j] = max(L[i+1][j], L[i][j-1])
        return L[0][n-1]
        """
        cl = 2:
            i = 0, j = 1
            i = 1, j = 2
            i = 2, j = 3
        cl = 3:
            i = 0, j = 2
            i = 1, j = 3
            i = 2, j = 4
            i = 3, j = 5
        cl = 4:
        cl = 5:
        """
        print(L)
