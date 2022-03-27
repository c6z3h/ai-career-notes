class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """ Solution Took Too Long
        k = k % len(nums)
        while (k>0):
            var = nums[len(nums)-1]
            for i in reversed(range(len(nums))):
                nums[i] = nums[i-1]
                #print(i, nums[i])
            nums[0] = var
            k-=1
            # if [1,2,3] > [3,1,2] > [2,3,1] > [1,2,3] k = 3 rotate len(nums) = 3
            # if [1,2,3,4] > [4123] > [3412] > [2341] > [1234] k = 4 rotate len(nums) = 4
        """
        n = len(nums)
        k = k%n
        nums[:] = nums[n-k:] + nums[:n-k]
