class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
        Example / Thought process:
        1. If a column has 0, whole column is zero. If a row has 0, whole row is zero.
        2. The above holds true no matter what.
        
        Algorithm:
        if matrix[i][j] == 0:
            rowSet.append(i)
            colSet.append(j)
        
        Reference:
        Got stuck and viewed NeetCode YouTube video before trying my own.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        row_zero_is_zero = False
        
        # Mark the First Row and Column with the places we need to ZERO
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    if r==0:
                        row_zero_is_zero = True
                    else:
                        matrix[0][c] = 0
                        matrix[r][0] = 0
        
        # Set ZEROs for all except 1st Row and Column (1st Cell)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        # Check if first column has to be set to ZERO
        if matrix[0][0] == 0:
            for r in range(ROWS):
                matrix[r][0] = 0
                
        # Check if first row has to be set to ZERO
        if row_zero_is_zero == True:
            for c in range(COLS):
                matrix[0][c] = 0
#         m = len(matrix)
#         if m == 0:
#             return
#         n = len(matrix[0])

#         row_zero = False
#         for i in range(m):
#             if matrix[i][0] == 0:
#                 row_zero = True
#         col_zero = False
#         for j in range(n):
#             if matrix[0][j] == 0:
#                 col_zero = True

#         for i in range(1, m):
#             for j in range(1, n):
#                 if matrix[i][j] == 0:
#                     matrix[i][0] = 0
#                     matrix[0][j] = 0

#         for i in range(1, m):
#             if matrix[i][0] == 0:
#                 for j in range(1, n):
#                     matrix[i][j] = 0

#         for j in range(1, n):
#             if matrix[0][j] == 0:
#                 for i in range(1, m):
#                     matrix[i][j] = 0

#         if col_zero:
#             for j in range(n):
#                 matrix[0][j] = 0
#         if row_zero:
#             for i in range(m):
#                 matrix[i][0] = 0
