class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        
        REACTO: Algorithm
        a resettable checker = [0]*9
        1. Check row: for each row, increment each index if number appears
            check list if any value > 1 return False
            reset the checker = [0]*9
        2. Check column: for each col, increment each index if number appears
            check list if any value > 1 return False
            reset the checker = [0]*9
        3. Check boxes: 
        """
        checker = [0]*9
        
        # 1. Check row
        for row in range(0,9):
            for col in range(0,9):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
            for index in range(0,9):
                if checker[index] > 1:
                    return False
            checker = [0]*9
        
        # 2. Check col
        for col in range(0,9):
            for row in range(0,9):
                if board[row][col] != ".":
                    value = int(board[row][col])
                    checker[value-1] += 1
            for index in range(0,9):
                if checker[index] > 1:
                    return False
            checker = [0]*9
            
        # 3. Check each box -- box 1
        for row in range(0,3):
            for col in range(0,3):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(0,3):
            for col in range(3,6):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(0,3):
            for col in range(6,9):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(3,6):
            for col in range(0,3):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(3,6):
            for col in range(3,6):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(3,6):
            for col in range(6,9):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(6,9):
            for col in range(0,3):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(6,9):
            for col in range(3,6):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        for row in range(6,9):
            for col in range(6,9):
                if board[row][col] != ".":
                    value = int(board[row][col]) # value between 1 and 9
                    checker[value-1] += 1
        for index in range(0,9):
            if checker[index] > 1:
                return False
        checker = [0]*9
        
        return True
                
