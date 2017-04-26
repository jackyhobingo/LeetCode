# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        self.get_hight(root)
        return self.ans
        
    def get_hight(self, root):
        if root == None:
            return 0
        left_h, right_h = self.get_hight(root.left), self.get_hight(root.right)
        self.ans = max(self.ans, left_h + right_h)
        return 1 + max(left_h, right_h)
