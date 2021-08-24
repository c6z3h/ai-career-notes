class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """
        #1: Brute Force Method
        for i in range(len(nums)):
            remainder = target - nums[i]
            for j in range(len(nums)):
                if i is not j and nums[j] == remainder:
                    return [i,j]
        """
        #2: Hash Table
        dict_remainder = {}
        for i in range(len(nums)):
            if nums[i] in dict_remainder:
                return [dict_remainder[nums[i]],i]
            remainder = target - nums[i]
            dict_remainder[remainder] = i
