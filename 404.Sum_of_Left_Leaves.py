# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        sum_ = 0
        right = [root.right] if root.right else []
        left = [root.left] if root.left else []
        while right or left:
            while right:
                node = right.pop()
                if node.right:
                    right.append(node.right)
                if node.left:
                    left.append(node.left)
            while left:
                node = left.pop()
                if not (node.right or node.left):
                    sum_ += node.val
                if node.right:
                    right.append(node.right)
                if node.left:
                    left.append(node.left)
        return sum_
