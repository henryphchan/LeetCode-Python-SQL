# https://leetcode.com/problems/middle-of-the-linked-list/
from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

if __name__ == '__main__':            
    s1 = Solution().middleNode(ListNode(2,ListNode(4,ListNode(3,None))))
    while s1:
        print(s1.val)
        s1 = s1.next