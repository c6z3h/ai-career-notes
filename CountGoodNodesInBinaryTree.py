# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.result = 0
        
        def recursive_check(current, val):
            if current.val >= val: self.result += 1
            if current.left is not None: recursive_check(current.left, max(val, current.val))
            if current.right is not None: recursive_check(current.right, max(val, current.val))
        
        recursive_check(root, root.val)
        
        return self.result
