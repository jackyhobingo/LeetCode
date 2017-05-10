# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        list_ = [root]
        ans = []
        for node in list_:
            if node:
                list_.extend([node.left, node.right])
                ans.append(str(node.val))
        return ' '.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        str_list = data.split(" ")
        root = TreeNode(int(str_list.pop(0)))

        for str_ in str_list:
            son = TreeNode(int(str_))
            cur = root
            while True:
                if cur.val > son.val:
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = son
                        break
                elif cur.val < son.val:
                    if cur.right:
                        cur = cur.right
                    else:
                        cur.right = son
                        break
        return root
    

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
