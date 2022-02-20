# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def end_of_first_half(self, head):
        """
        :param head: head of ListNode
        :return: the middle position
        """
        fast = head
        slow = head
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
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

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # list = []
        # while head:
        #     list.append(head.val)
        #     head = head.next
        # flag = True
        # listLen = len(list)
        # for i in range(listLen//2):
        #     if list[i] != list[-i-1]:
        #         return False
        # return True
        if head is None:
            return True

        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverseList(first_half_end.next)

        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        first_half_end.next = self.reverseList(second_half_start)
        return result





n5 = ListNode(val=1)
n4 = ListNode(val=2, next=n5)
n3 = ListNode(val=2, next=n4)
n2 = ListNode(val=2, next=n3)
n1 = ListNode(val=1, next=n2)

# n1 = ListNode(val=1)

head = n1
s = Solution()
result = s.isPalindrome(head)

print(result)