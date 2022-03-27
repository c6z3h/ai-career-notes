class Solution:
    def longestConsecutive(self, nums):
        """
        You want O(n) time...
        list solution: Time Limit Exceeded.
        need a set()
        """
        nums = set(nums)
        maxlen = 0
        
        while nums:
            first = last = nums.pop()
            while last + 1 in nums:
                nums.remove(last+1)
                last += 1
            while first - 1 in nums:
                nums.remove(first-1)
                first -= 1
            maxlen = max(maxlen, last - first + 1)
            
        return maxlen
