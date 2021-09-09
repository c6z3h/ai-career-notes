class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        
        Example:
        - if intervals are identical :: remove the copies.
        - if intervals do not overlap :: do nothing
        - if intervals overlap :: 
            - but first, define what is overlap ::
                1. intervals[i][1] > intervals[i+1][0] eg. [1,2][2,3] is ok
                2. order to remove? eg. [1,3][1,6][3,6]
                    hypothesis: always better to remove the largest range [1,6]. it will likely overlap with the most intervals.
                    
        Algorithm:
        1. sort intervals.
        2. convert to set, then convert to list again. # remove duplicates
        3. loop: if intervals[i][0] == intervals[i+1][0]: remove intervals[i+1]; count+=1
        4. check remaining intervals no overlap: intervals[i][1] > intervals[i+1][0]
        5. return count
        """
        intervals.sort(key = lambda x: x[1])
        max_end = - 50000
        res = 0
        
        for start,end in intervals:
            if start >= max_end:
                max_end = end
            else:
                res += 1
                
        return res
