# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        newHead = ListNode(-1)
        newHead.next = head
        
        prev, curr = None, head
        i = 0
        while i < n:
            prev = curr
            curr = curr.next
            i += 1

        prev, slow = newHead, head
        while curr:
            prev = slow
            slow = slow.next
            curr = curr.next

        prev.next = slow.next
        return newHead.next