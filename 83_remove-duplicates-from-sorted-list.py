# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = ListNode(-101, None)
        cur = head
        while (cur):
            #print(cur.val, prev.val)
            if prev.val == cur.val:
                pass
            else:
                prev.next = cur
                prev = prev.next
            cur = cur.next
        prev.next = None
        return head

if __name__ == '__main__':
    s = Solution()
    l = ListNode(1)
    l.next = ListNode(1)
    l.next.next = ListNode(2)
    l.next.next.next = ListNode(3)
    l.next.next.next.next = ListNode(3)
    ans = s.deleteDuplicates(l)
    while ans:
        print(ans.val, end=" ")
        ans = ans.next