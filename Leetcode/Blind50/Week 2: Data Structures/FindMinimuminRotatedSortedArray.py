class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        REACTO
        Optimize:
        1. min() operation
            Time: O(n)
            Space: O(1)?
        2.
        """
        # return min(nums)
        
        if len(nums)==1:
            return nums[0]
        
        if nums[0] < nums[1] and nums[0] < nums[-1]:
            return nums[0]
        
        l,r = 0,len(nums)-1
        while l < r:
            midpoint = l + (r-l)//2
            if nums[midpoint] > nums[l]:
                l = midpoint
            else:
                r = midpoint
        
        return nums[l+1]
