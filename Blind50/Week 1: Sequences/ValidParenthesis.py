class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_p = {'{':'}','[':']','(':')'}
        n = len(s)
        # { [ ( must have ) ] }
        # stack.append: } ] )
        if n < 2:
            return False
        
        stack = []
        for i in range(n):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                stack.append(dict_p[s[i]])
            elif stack == [] or s[i] != stack[-1]:
                return False
            else:
                stack.pop()
                
        if stack == []:
            return True
        
        return False
