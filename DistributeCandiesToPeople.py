class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        BRUTE FORCE METHOD
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        liste = [0]*num_people
        counter = 1
        pointer = 0
        while (candies>0):
            if (pointer == len(liste)-1):
                if counter > candies:
                    liste[pointer] += candies
                else:
                    liste[pointer] += counter
                candies -= counter
                counter = counter + 1
                pointer = 0
            else:
                if counter > candies:
                    liste[pointer] += candies
                else:
                    liste[pointer] += counter
                candies -= counter
                counter += 1
                pointer += 1
        return liste
