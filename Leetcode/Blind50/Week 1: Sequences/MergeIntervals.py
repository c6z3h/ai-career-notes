class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        
        Repeat
        Example: if [1,5][4,7] is overlap, if [1,5][5,7] is overlap, if [1,5][6,7] is not.
        Algorithm: if intervals[i][1] >= intervals[i+1][0] then merge, append to separate array. Then, i += 1 because we can skip the next array
            - but we need to store in a separate array as a for-loop might run ConcurrentModificationError.
            - else append intervals[i] and iterate next
            * OH WAIT. If there are 3 overlapping intervals in a row... maybe store in a temporary list variable first. If confirm not overlapping anymore THEN append to list.
        Code...
        
        vv DIDN'T DO THIS! vv
        Test (edge cases):
            - [1,3]
            - [1,4][0,4]
            - [1,4][0,0]
        
        Optimize:
            - Time: O(nlogn) for sorted() and O(n) for for-loop == O(n) worst
            - Space: O(1) to store n, O(n) worst case to store return_list
        """
        n = len(intervals)
        intervals = sorted(intervals)
        return_list = []
        
        if n == 1:
            return intervals
        
        for i in range(n-1):
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [min(intervals[i][0],intervals[i+1][0]),max(intervals[i+1][1],intervals[i][1])]
                if i == n-2:
                    return_list.append(intervals[i+1])
            else:
                return_list.append(intervals[i])
                if i == n-2:
                    return_list.append(intervals[i+1])
        
        # at i = n-3 if merge intervals[i-2] = [a,b]
        # loop again, i = n-2 (last pass)
        # if its a merge, intervals[n-1] = [a,b] but not appended to return_list (OK)
        # if its a remain the same, intervals[n-1] is left out of list. (?)
        
        return return_list
