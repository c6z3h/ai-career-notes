# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low  = 1
        high = n
        
        while low < high:
            mid = (high - low) // 2 + low
            if isBadVersion(mid) is False:
                low = mid + 1
            else:
                high = mid
        return low
