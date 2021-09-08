class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        
        Example:
        - sort ascending.
        """
        nums.sort()
        res = []
        # -1 -1 0 1 2
        for i,a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
            
            l,r = i+1,len(nums)-1
            
            while l < r:
                three_sum = a + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
        
        return res
