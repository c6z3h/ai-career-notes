class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # Highest Power of 3 within Limits: 1162261467
        return (n > 0 and 1162261467%n == 0)
