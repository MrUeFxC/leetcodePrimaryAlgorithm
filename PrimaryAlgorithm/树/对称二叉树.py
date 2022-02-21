# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.check(root.left, root.right)
    def check(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.check(p.left, q.right) and self.check(p.right, q.left)



t5 = TreeNode(val=4)
t4 = TreeNode(val=4)
t3 = TreeNode(val=2,left=t4, right=t5)
t7 = TreeNode(val=4)
t6 = TreeNode(val=3)
t2 = TreeNode(val=2, left=t6, right=t7)
t1 = TreeNode(val=1, left=t2, right=t3)

# t1 = TreeNode(val=1)

s = Solution()
result = s.isSymmetric(t1)
print(result)