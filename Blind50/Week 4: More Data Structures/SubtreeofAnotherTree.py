# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        if subRoot is None:
            return True
        if root is None and subRoot is not None:
            return False
        return self.issame(root,subRoot) or self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    
    def issame(self, s, t):
        if s is None and t is None:
            return True
        if s is None and t is not None:
            return False
        if s is not None and t is None:
            return False
        return s.val == t.val and self.issame(s.left,t.left) and self.issame(s.right,t.right)
