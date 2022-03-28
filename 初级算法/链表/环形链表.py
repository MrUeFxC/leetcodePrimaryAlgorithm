# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False

n5 = ListNode(val=1)
n4 = ListNode(val=2, next=n5)
n3 = ListNode(val=2, next=n4)
n2 = ListNode(val=2, next=n3)
n1 = ListNode(val=1, next=n2)
n5.next = n1

# n1 = ListNode(val=1)

head = n1
s = Solution()
result = s.hasCycle(head)

print(result)