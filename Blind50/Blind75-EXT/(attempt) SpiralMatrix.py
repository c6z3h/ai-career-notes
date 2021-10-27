# Attempt
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
        1 2 3 4 5 6 7 8 9 .
        . 6 7 8 5 2 3 4 . 6
        9 . 1 2 1 2 3 . 7 3
        1 2 3 4 5 6 7 8 9 0
        5 6 7 8 5 2 3 4 5 6
        9 0 1 2 1 2 3 6 7 3
        1 2 3 4 5 6 7 8 9 0
        5 6 7 8 5 2 3 . 5 6
        9 . 1 2 1 2 3 6 . 3
        . 6 7 8 5 2 3 4 5 .
        
        ROW = LEN()-1, COL = LEN()-1
        > (0,COL)
        V (ROW,COL)
        < (ROW,0)
        ^ (1,0)
        ----
        > (1, COL-1)
        V (ROW-1,COL-1)
        < (ROW-1,1)
        ^ (2,1)
        ----
        > (2,COL-2)
        V (ROW-2,COL-2)
        < (ROW-2,2)
        ^ (3,2)
        ROW, COL = len(matrix)-1,len(matrix[0])-1
        turning_point = {"right": [0,COL], "down": [ROW,COL], "left": [ROW,0], "up":[1,0]}
        # at each turn, "right" += [1,-1], "down" += [-1,-1], "left" += [-1,1], "up" += [1,1]
        # if next turning_point is same as current turning point, stop.
        1 2 .
        . . 7
        9 . 1
        . 2 .
        (0,2) - (3,2) - (3,0) - (1,0)
        (1,1) - (2,1) - (2,1) - (2,1)
        (2,0)* - (1,0)
        
        def spiral_walk(r,c,turn_r,turn_c):
        1. move right
        2. turn at turn_r, turn_c = 0,len(matrix[0])-1
        3. move down
        4. turn at turn_r, turn_c = len(matrix)-1,len(matrix[0])-1
        5. move left
        6. turn at turn_r, turn_c = len(matrix)-1,0
        7. move up
        8. turn at turn_r, turn_c = len(matrix)-1-1,0
        
        """
        res = []
        # 1. The movement stuff, until it hits the turning point.
        movements = {"right": [0,1], "down": [1,0], "left": [0,-1], "up": [-1,0]}
        r,c = 0,0
        add_r,add_c = movements["right"]
        r += add_r
        c += add_c
        print(r,c)
        res.append(matrix[r][c])
        
        # 2. Turning point
        ROW, COL = len(matrix)-1,len(matrix[0])-1
        
        # Edge Case: 1 element
        if ROW == 0 and COL == 0: return matrix[0][0]
        
        turning_point = {"right": [0,COL], "down": [ROW,COL], "left": [ROW,0], "up":[1,0]}
        direction_to_int = {"right": 1, "down": 2, "left": 3, "up":4}
        # at each turn, "right" += [1,-1], "down" += [-1,-1], "left" += [-1,1], "up" += [1,1]
        # if next turning_point is same as current turning point, stop.
        
        # 3. recursion
        def spiral_walk(r,c,turn_r,turn_c,movement):
            # a. Exit condition
            if movement == "right":
                if turning_point["right"] == turning_point["up"]: return
            if movement == "down":
                if turning_point["down"] == turning_point["right"]: return
            if movement == "left":
                if turning_point["left"] == turning_point["down"]: return
            if movement == "up":
                if turning_point["up"] == turning_point["left"]: return
                
                    
            
        # 4. call recursion
        spiral_walk(0,0,_,_,"right")
