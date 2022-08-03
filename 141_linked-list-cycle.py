# https://leetcode.com/problems/linked-list-cycle/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer = head
        listDict = {}
        if head is None: return False
        while pointer.next:
            if listDict.get(pointer) is not None:
                return True
            listDict[pointer] = 1
            pointer = pointer.next
        return False

if __name__ == '__main__':
    s = Solution()
    l = ListNode(1)
    lr = l.next = ListNode(2)
    l.next.next = ListNode(3)
    l.next.next.next = lr
    print(s.hasCycle(l))