class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        
        1. identify if the numbers are rotated - compare value of index (0,-1,1)
            unrotated: [-5 0 5]             == nums[0] < nums[1] and nums[0] < nums[-1]
            rotated: [5 -5 0]               == nums[0] > nums[1] and nums[0] > nums[-1]
                  or [0 5 -5]               == nums[0] < nums[1] and nums[0] > nums[-1]
           #pattern: if rotated nums[0] > nums[-1]
            
            unrotated: [-5 -2 0 2 5]        == nums[0] < nums[1] and nums[0] < nums[-1]
            rotated:   [5 -5 -2 0 2]        == nums[0] > nums[1] and nums[0] > nums[-1]
                       [2 5 -5 -2 0]        == nums[0] < nums[1] and nums[0] > nums[-1]
                       [0 2 5 -5 -2]        == nums[0] < nums[1] and nums[0] > nums[-1]
                       [-2 0 2 5 -5]        == nums[0] < nums[1] and nums[0] > nums[-1]
           #pattern: if rotated nums[0] > nums[-1]
           #time_complexity: O(1)
        
        2. set l,r pointers
            (a) if unrotated, l,r = 0,len(nums)-1
            (b) if rotated, do once binary search to find minimum value's INDEX.
                l,r = INDEX,INDEX-1
                
            #time_complexity: O(logn)
            
        3. actions based on rotation:
        (a) if unrotated
            a) if target exist between indexes, binary search
            b) else return -1
        (b) if rotated
            a) if target between nums[0] and nums[r], binary search
            b) if target between nums[l] and nums[-1], binary search
            c) else return -1
            
            #time_complexity: O(logn)
        """
        # 1. Handle edge cases with nums.length <= 3
        if len(nums) <= 3:
            if target not in nums: return -1
            else:
                for i,a in enumerate(nums):
                    if a == target: return i
        
        # 2. Binary Search Function
        def binary_search(array, target):
            l,r = 0,len(array)-1
            if target == array[l]: return l
            if target == array[r]: return r
            while r-l>1:
                mid = (r+l)//2
                if target > array[mid]:
                    l = mid
                elif target < array[mid]:
                    r = mid
                else: # target == nums[mid]
                    return mid
            if target == array[l]: return l
            if target == array[r]: return r
            return -1
        
        # 3. Determine if nums is rotated
        rotated = False
        if nums[0] > nums[-1]:
            rotated = True
        
        # 4. Set (l)eft and (r)ight pointers
        l,r = 0,len(nums)-1
        if rotated == True:
            while r-l>1:
                mid = (r+l)//2
                if nums[mid] > nums[l]:
                    l = mid
                else:
                    r = mid
            if r == mid: l,r = mid,mid-1
            elif l == mid: l,r = mid+1,mid
        
        # 5. Perform action according to (un)rotation status
        res = 0
        if rotated == False:
            if target >= nums[l] and target <= nums[r]:
                res = binary_search(nums, target)
            else: return -1
        else:
            if target >= nums[0] and target <= nums[r]:
                res = binary_search(nums[0:r+1], target)
            elif target >= nums[l] and target <= nums[-1]:
                res = binary_search(nums[l:], target)
                if res != -1: res += l
            else: return -1
        
        return res
