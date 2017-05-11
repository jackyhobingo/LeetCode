# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def rob(node):  # result = (max(contain, not contain node), not contian node)
            if not node:
                return 0, 0
            l = rob(node.left)
            r = rob(node.right)
            return max(node.val + l[1] + r[1], l[0] + r[0]), l[0] + r[0]
        return rob(root)[0]
