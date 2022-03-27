class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        
        hmap = {}
        for num in nums:
            hmap[num] = 1 + hmap.get(num, 0)
            
        while k > 0:
            max_val = max(hmap, key = hmap.get)
            res.append(max_val)
            del(hmap[max_val])
            k -= 1
        
        return res
