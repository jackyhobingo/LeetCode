# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = -2 ** 31
        self.findMaxPath(root)
        return self.max
        
    def findMaxPath(self, root):
        
        if root == None:
            return 0
        r = max(self.findMaxPath(root.right), 0)
        l = max(self.findMaxPath(root.left), 0)
        self.max = max(self.max, root.val + r + l)
        return root.val + max(r, l)
