class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        count1 = [0] * 1001; count2 = [0] * 1001; rlist = []
        for i in range(len(nums1)):
            count1[nums1[i]] += 1
        for j in range(len(nums2)):
            count2[nums2[j]] += 1
        for n in range(1001):
            if (count1[n] != 0 and count2[n] != 0):
                while (count1[n] > 0 and count2[n] > 0):
                    rlist.append(n)
                    count1[n] -= 1; count2[n] -= 1;
        return rlist
