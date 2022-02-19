# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        newHead = ListNode(None,head)
        left = newHead
        right = newHead
        while right:
            if n > 0:
                right = right.next
                n -= 1
                continue
            if right.next == None:
                left.next = left.next.next
                break
            right = right.next
            left = left.next

        return newHead.next


n5 = ListNode(val=5)
n4 = ListNode(val=4, next=n5)
n3 = ListNode(val=3, next=n4)
n2 = ListNode(val=2, next=n3)
n1 = ListNode(val=1, next=n2)

# n1 = ListNode(val=1)

head = n1
s = Solution()
result = s.removeNthFromEnd(head,5)

list = []
while result:
    list.append(result.val)
    result = result.next
print(list)