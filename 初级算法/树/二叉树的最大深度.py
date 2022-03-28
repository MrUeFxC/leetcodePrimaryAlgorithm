# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return  max(left , right) + 1




t5 = TreeNode(val=7)
t4 = TreeNode(val=15)
t3 = TreeNode(val=20, left=t4, right=t5)
t2 = TreeNode(val=9)
t1 = TreeNode(val=3, left=t2, right=t3)

s = Solution()
result = s.maxDepth(t1)

print(result)