class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Example:
        - if n == 1: return nums[0]
        - gen case : left pointer, move right pointer
            - if 2nd digit > sum, move left pointer over.
        """ 
        # 1. Unelegent Kadane's Algorithm
#         n = len(nums)
#         if n == 1:
#             return nums[0]
        
#         l = 0
#         res_sum = nums[l]
#         max_sum = res_sum
#         for i in range(1,n):
#             if res_sum+nums[i] <= nums[i]:
#                 l = i
#                 res_sum = nums[l]
#             else:
#                 res_sum += nums[i]
#             max_sum = max(max_sum, res_sum)
        
#         return max_sum
    
        # 2. Dynamic Programming... Kadane's Algorithm
        n = len(nums)
        sum_of_elements = 0
        max_sum = -100000
        for i in range(n):
            sum_of_elements += nums[i]
            sum_of_elements = max(nums[i], sum_of_elements)
            
            max_sum = max(max_sum, sum_of_elements)
        
        return max_sum
