# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ans = []
        q = [root] if root else None
        while q:
            nexts = []
            ans.append(max([node.val for node in q]))
            while q:
                node = q.pop()
                if node.left:
                    nexts.append(node.left)
                if node.right:
                    nexts.append(node.right)
            q.extend(nexts)
        return ans
