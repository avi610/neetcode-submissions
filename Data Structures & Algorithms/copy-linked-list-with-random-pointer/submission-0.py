import heapq

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copies = {}

        newHead = Node(-1)
        prev, curr = newHead, head

        while curr:
            currCopy = Node(curr.val)
            copies[curr] = currCopy
            prev.next = currCopy
            prev = currCopy
            curr = curr.next

        currCopy, curr = newHead.next, head
        while curr and currCopy:
            if curr.random and curr.random in copies:
                currCopy.random = copies[curr.random]
            curr = curr.next
            currCopy = currCopy.next

        return newHead.next