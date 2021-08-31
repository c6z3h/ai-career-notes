class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        pre_product = [1]*n
        post_product = [1]*n
        product = [0]*n
        #PRE_P: 1  1  2 6
        #POS_P: 24 12 4 1
        #MULTI: 24 12 8 6
        
        for i in range(1,n):
            pre_product[i] = pre_product[i-1] * nums[i-1]
            post_product[-(i+1)] = post_product[-i] * nums[-i]
        # for i in range(n-2,-1,-1):
        #     post_product[i] = post_product[i+1] * nums[i+1]
            
        for i in range(n):
            product[i] = pre_product[i] * post_product[i]
            
        return product
