# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resHead = ListNode(-1)
        a, b, carry, res = l1, l2, 0, resHead
        while a or b or carry:
            aVal = a.val if a else 0
            bVal = b.val if b else 0
            val = aVal + bVal + carry
            res.next = ListNode(val%10)
            carry = val//10
            if a:
                a = a.next
            if b:
                b = b.next
            res = res.next

        return resHead.next