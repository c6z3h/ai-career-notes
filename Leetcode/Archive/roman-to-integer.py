class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = 0
        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,
             "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        
        # TEST CASE: MCMXCIV         len(s) = 7      range = 7 {0,1,2,3,4,5,6}     romanNum = IV   i = 7
        # value = 1994
        # M C M X C I V
        # 0 1 2 3 4 5 6
        # 1. loop through the two letters: if match, += the value
        
        i = 0
        while i < len(s):
            romanNum = s[i]
            if i+1 <= len(s) -1:
                romanNum += s[i+1]
            if (len(romanNum)==2) and (romanNum in d):     
                value += d[romanNum]
                i += 2
        # 2. after that, loop through single letters
            else:
                romanNum = s[i]
                value += d[romanNum]
                i += 1
        return value
        
