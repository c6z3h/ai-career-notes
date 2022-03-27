class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        """
        # 70 / 91 Test Cases Passed.
        # Only char: '()[]{}'
        # ([)] is wrong, [()] is right.
        # By extension: { { [ { { { } } } ] } } is right, and { { [ { { { } } } } } ] is wrong.
        # Index:        0 1 2 3 4 5 6 -5 -4 -3 -2 -1
        d = {"(": 3, ")": -3,"{": 2,"}": -2,"[": 1,"]": -1}
        if len(s)%2 != 0:
            return False
        for i in range(len(s)//2):
            if d[s[i]] + d[s[-(i+1)]] != 0:
                return False
        return True
        """
        # CREATIVE SOLUTION
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace("{}", "").replace("[]", "")
        return s == ''
