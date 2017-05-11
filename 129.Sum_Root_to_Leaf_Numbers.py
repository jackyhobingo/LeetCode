# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def sumNumbers(root, sum):
            if not root:
                return
            sum = sum * 10 + root.val
            if root.right == root.left == None:
                self.ans += sum
            sumNumbers(root.right, sum)
            sumNumbers(root.left, sum)
        sumNumbers(root, 0)
        return self.ans
