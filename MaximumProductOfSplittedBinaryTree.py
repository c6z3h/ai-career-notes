# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        REACTO: (E)xample: How to get maximum product? Ensure that both subtrees have similar sum.
        If m->1 and n -> infinity :         m*n -> infinity
        If m->infinity and n -> 1 :         m*n -> infinity
        If m->infinity/2 and n->infinity/2: m*n -> infinity^2/4
        
        (E)dge cases:
        1. 2 nodes only. then just split.
        
        (A)lgorithm:
        """
        
        sums = []
        def treeSum(node):
            if node is None:
                return 0
            subtree_sum = treeSum(node.left) + treeSum(node.right) + node.val
            sums.append(subtree_sum)
            return subtree_sum
        
        total_sum = treeSum(root)
        m = 0
        for i in sums:
            product = (total_sum - i) * i
            if product > m: m = product
        return m % (10**9 + 7)
