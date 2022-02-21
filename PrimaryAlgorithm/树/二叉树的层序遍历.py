# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        res = []
        while queue:
            length = len(queue)
            sub_list = []
            for i in range(length):
                node = queue.pop(0)
                sub_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sub_list)
        return res
        

t5 = TreeNode(val=4)
t4 = TreeNode(val=4)
t3 = TreeNode(val=2,left=t4, right=t5)
t7 = TreeNode(val=4)
t6 = TreeNode(val=3)
t2 = TreeNode(val=2, left=t6, right=t7)
t1 = TreeNode(val=1, left=t2, right=t3)

# t1 = TreeNode(val=1)

s = Solution()
result = s.levelOrder(t1)
print(result)