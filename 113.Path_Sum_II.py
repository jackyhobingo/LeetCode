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
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(list_, root, target):
            if root == None:
                return 
            elif target == root.val and root.right == root.left == None:
                ans.append(list_ + [root.val])
            else:
                dfs(list_ + [root.val], root.right, target - root.val)
                dfs(list_ + [root.val], root.left, target - root.val)
        dfs([], root, sum)
        return ans
