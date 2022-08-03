# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        headList = []
        
        while head is not None:
            headList.append(head.val)
            head = head.next
         
        if headList == headList[::-1]:
            return True
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    l = ListNode(1,None)
    l.next = ListNode(2,None)
    l.next.next = ListNode(2, None)
    l.next.next.next = ListNode(1,None)
    print(s.isPalindrome(l))