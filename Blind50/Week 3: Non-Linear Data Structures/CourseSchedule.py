class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        Example:
        - 1 course: false
        - 2 course: [0,1][1,0] = false. [1,0] or otherwise = true
        - 3 course: [0,1][1,0] = false. [0,1][0,2][2,1], [0,1][1,2] = true
        
        * If len(prereq) == numCourses: false NOT TRUE.
        * deal breaker: false IF AND ONLY IF [a,b][b,a] or.. [a,b][b,c][c,a]
        """
        visit_set = set()
        courses = {i:[] for i in range(numCourses)}
        
        for crs,pre in prerequisites:
            courses[crs].append(pre)
            
        def dfs(crs):
            if crs in visit_set:
                return False
            if courses[crs] == []:
                return True
            visit_set.add(crs)
            for pre in courses[crs]:
                if not dfs(pre): return False
            visit_set.remove(crs)
            courses[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        return True
