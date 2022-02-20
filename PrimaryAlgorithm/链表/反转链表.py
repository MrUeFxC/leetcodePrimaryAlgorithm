# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # if head == None:
        #     return None
        # listReverse = []
        # while head:
        #     listReverse.append(head)
        #     head = head.next
        #
        # listLen = len(listReverse)
        # for i in range(listLen):
        #     if i < listLen - 1:
        #         listReverse[listLen - i - 1].next = listReverse[listLen - i - 2]
        #     else:
        #         listReverse[listLen - i - 1].next = None
        # head = listReverse[listLen - 1]
        # return head
        pre = None
        cur = head
        while cur:
            # 先找到下一个数
            tmp = cur.next
            # 把现在的数指向之前的数
            cur.next = pre
            # pre 和 cur 同时向前一格
            pre = cur
            cur = tmp
        return pre


n5 = ListNode(val=5)
n4 = ListNode(val=4, next=n5)
n3 = ListNode(val=3, next=n4)
n2 = ListNode(val=2, next=n3)
n1 = ListNode(val=1, next=n2)

# n1 = ListNode(val=1)

# n1 = None

head = n1
s = Solution()
result = s.reverseList(head)

list = []
while result:
    list.append(result.val)
    result = result.next
print(list)
