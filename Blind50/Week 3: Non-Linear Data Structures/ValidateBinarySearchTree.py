# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        
        """
        MIN,MAX = float('-inf'), float('inf')
        
        def dfs(node, MIN, MAX):
            if not node:
                return True
            val = node.val
            if val <= MIN or val >= MAX:
                return False
            return dfs(node.left,MIN,val) and dfs(node.right,val,MAX)
        
        return dfs(root, MIN, MAX)
