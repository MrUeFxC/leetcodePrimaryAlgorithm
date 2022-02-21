# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    preV = None
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        if not self.isValidBST(root.left):
            return False
        if self.preV is not None and self.preV.val > root.val:
            return False
        self.preV = root
        if not self.isValidBST(root.right):
            return False
        return True





t5 = TreeNode(val=7)
t4 = TreeNode(val=15)
t3 = TreeNode(val=3,left=t4, right=t5)


t6 = TreeNode(val=0)
t2 = TreeNode(val=1, left=t6)
t1 = TreeNode(val=2, left=t2, right=t3)

s = Solution()
result = s.isValidBST(t1)

print(result)