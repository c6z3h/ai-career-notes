class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        
        Repeat -- strings contain exactly same letters == True.
        Example -- is length of "s" always equal "t"? No, check it.
        Algorithm -- (0) if len(t) not len(s) return False (1) sort the strings (2) check if strings equal.
        Code
        Test
        Optimize (Complexity) -- Space: O(1) for n, m. s, t sorted in place. Time: sorting algoritm takes O(nlogn) for                                        Timsort. It could be worse if we add each letter in each string to a list. Or am
                                 I overthinking? Let's see the "Discussion" page...Yes I have the optimized one.
        """
        n = len(s)
        m = len(t)
        
        if n != m:
            return False
        
        s = sorted(s)
        t = sorted(t)

        if s == t:
            return True
        return False
