class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        Exceeded Time Limit
        for i in range(len(nums)):
            j = 0
            while (j<len(nums)):
                if (i != j and nums[i] == nums[j]):
                    break
                j+=1
            if (j == len(nums)):
                return nums[i]
        """
        count = [0] * 60001 # Note that range of nums[i] is between +/- 30_000
        for i in range(len(nums)):
            count[nums[i]]+=1
            
        for i in range(len(nums)):
            if count[nums[i]] == 1:
                return nums[i]
