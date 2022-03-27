class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        Error at: "dvdf"
        Test cases passed: 444 / 987
        """
        if len(s) == 0:
            return 0
        
        longest_string = []
        return_value = 0
        for j in range(len(s)):
            for i in range(j, len(s)):
                if s[i] not in longest_string:
                    longest_string.append(s[i])
                else:
                    max_value = len(longest_string)
                    if max_value > return_value:
                        return_value = max_value
                    longest_string = []
                    longest_string.append(s[i])
                if i == len(s) - 1 - j:
                    max_value = len(longest_string)
                    if max_value > return_value:
                        return_value = max_value
                    longest_string = []
        print(longest_string)
        return return_value
