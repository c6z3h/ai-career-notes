class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        
        Algorithm:
        - two pointers (l,r)
        - each time count # replacements
        - if replacement > k; move l-pointer
        """
        seen = {}
        l,count = 0,0

        for r in range(len(s)):
            seen[s[r]] = 1 + seen.get(s[r], 0)
            
            while (r-l+1)-max(seen.values()) > k:
                seen[s[l]] -= 1
                l += 1
            
            count = max(count, r-l+1)
        return count
