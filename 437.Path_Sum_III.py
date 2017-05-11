# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.find_root_sum(root, sum) + self.pathSum(root.right, sum) + self.pathSum(root.left, sum)

    def find_root_sum(self, root, sum):
        if not root:
            return 0
        sum -= root.val
        return int(sum == 0) + self.find_root_sum(root.left, sum) + self.find_root_sum(root.right, sum)
