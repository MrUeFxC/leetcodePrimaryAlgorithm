# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        LLLoc = 0
        LRLoc = 0

        # newList = ListNode(0)
        # head = ListNode(0,newList)
        # while list1 or list2:
        #     if list1 != None:
        #         val1 = list1.val
        #     else:
        #         while list2:
        #             newList.next = list2
        #             newList = newList.next
        #             list2 = list2.next
        #         break
        #     if list2 != None:
        #         val2 = list2.val
        #     else:
        #         while list1:
        #             newList.next = list1
        #             newList = newList.next
        #             list1 = list1.next
        #         break
        #     if val1 <= val2:
        #         newList.next = list1
        #         newList = newList.next
        #         list1 = list1.next
        #     else:
        #         newList.next = list2
        #         newList = newList.next
        #         list2 = list2.next
        # return head.next.next

        prehead = ListNode(-1)
        prev = prehead
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        prev.next = list1 if list1 is not None else list2
        return prehead.next



LL3 = ListNode(val=4, next=None)
LL2 = ListNode(val=2, next=LL3)
LL1 = ListNode(val=1, next=LL2)

LR3 = ListNode(val=4, next=None)
LR2 = ListNode(val=3, next=LR3)
LR1 = ListNode(val=1, next=LR2)

s = Solution()
result = s.mergeTwoLists(LL1,LR1)

list = []
while result:
    list.append(result.val)
    result = result.next
print(list)