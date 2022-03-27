class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Repeat
        Example:
        - base case: len(strs) <= 1 return [strs] 
        - gen case: (quite straightforward)
        - edge case: -
        Algorithm:
        OK Copy strs to new_array. For-loop, sort letters within each new_array[i].
        OK for loop: get "index" of identical strings.
        OK store used indexes in a set, to ensure no repeats.
        - return_list.append(strs["index"es])
        Code:...
        Test:
        - ["eat","tea","tan","ate","nat","bat"]
        - n = 6, strs_copy = ["ate","ate","ant","ate","ant","abt"]
        - index_list = [ [0,1,3], index_list[1]?, [2,4],index_list[3]?,index_list[4]?,[5]]
        - used_index = {0,1,2,3,4,5}
        - m = 6
        - return_list = [["eat","tea","ate"]]
        Optimize:
        - Time: O(n**2) because "for i in range(n): for j in range(n)"
        - NOT because of "for i in range(m): for index in index_list[i]:"
        - Space: O(n) to strs_copy, O(n) for used_index, O(n) for index_list, O(n) for return_list :: O(n)
        - CAN IMPROVE on time: Use HashTable? for the O(n**2) loop...
        - O(n) for loop to store in hashtable
        - (should think somemore)
        """
        n = len(strs)
        strs_copy = strs[:]
        used_index = set()
        index_list = []
        return_list = []

        for i in range(n):
            strs_copy[i] = sorted(strs_copy[i])

        for i in range(n):
            temp_index_list = []
            if i not in used_index:
                # index_list[i] = [i]
                temp_index_list.append(i)
                used_index.add(i)
                for j in range(n):
                    if strs_copy[j] == strs_copy[i] and i != j: #and j not in used_index:
                        temp_index_list.append(j)
                        used_index.add(j)
                index_list.append(temp_index_list)

        # Result should look something like index_list = [[1,4,5],[2,3,6]]
        m = len(index_list)

        for i in range(m):
            temp_anagram_list = []
            for index in index_list[i]:
                temp_anagram_list.append(strs[index])
            return_list.append(temp_anagram_list)
        
        return return_list
