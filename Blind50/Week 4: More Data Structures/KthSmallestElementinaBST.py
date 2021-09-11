# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        
        Algorithm:
        1. Do a depth-first search
        2. store all values into a list_vals, exclude nulls.
        3. return list_vals[k]
        """
        list_val = []
        
        def dfs(node):
            if not node:
                return
            if node.val not in list_val:
                list_val.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        list_val.sort()
        return list_val[k-1]
