class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        
        HINT: Sliding Window Approach
        NOTE: Almost there...
        """
        # Edge cases
        if len(t) == 0 or len(t) > len(s):
            return ""
        
        # Looks like a dynamic programming question...
        # Pointers i,j,k to iterate. i for start and j for end of String, k is pointer.

        # Check if whole s contains t.
        temp_t = list(t)
        print(temp_t)
        for i in range(len(s)):
            if s[i] in temp_t:
                temp_t.remove(s[i])
        
        if not temp_t:
            print("String s contains substring t!")
            min_string = s
        else:
            return ""
        
        # Shortening the substring.
        max_start_index = len(s)-len(t)+1 # This first pointer must lie between index 0 to max_start_index
        for i in range(max_start_index):
            temp_t = list(t)
            if s[i] in temp_t:
                    temp_t.remove(s[i])
            # Check the minimum string s length, by gradualling reducing pointer "j"
            for j in range(len(s)-1, i+1, -1):
            # for j in range(i+1, len(s)):
                for k in range(i+1,j+1):
                    if not temp_t:
                        current_string = s[i:j]
                    if s[k] in temp_t:
                        temp_t.remove(s[k])
                if len(current_string)<len(min_string):
                    min_string = current_string
        return min_string
        # for i in range(len(s)-len(t)+1):
        #     current_sum = 0
        #     for j in range(len(t)):
        #         current_sum += arr[i+j]
        #     max_sum = max(max_sum, current_sum)
