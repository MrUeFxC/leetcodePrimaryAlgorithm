class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


head = [4,5,1,9]
listNode = []
listNode.append(ListNode.__init__(head))
node = 1
s = Solution()
result = s.deleteNode(node)
print(result)