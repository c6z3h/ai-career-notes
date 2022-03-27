class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Learning Points:
            * Convert Int to String before indexing
        """
        number = 0
        for i in range(len(digits)):
            number += 10**i*digits[-(i+1)]
        number_new = number + 1
        if len(str(number_new)) > len(str(number)):
            digits.append(0)
        for i in range(len(str(number_new))):
            digits[i] = str(number_new)[i]
        return digits
