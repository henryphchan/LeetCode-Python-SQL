# https://leetcode.com/problems/merge-two-sorted-lists/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        
        if list1 == None : 
            minVal = list2.val
            sorted = self.mergeTwoLists(None,list2.next)
        if list2 == None : 
            minVal = list1.val
            sorted = self.mergeTwoLists(list1.next,None)

        if list1 != None and list2 != None:
            if list1.val > list2.val:
                minVal = list2.val
                sorted = self.mergeTwoLists(list1,list2.next)
            else:
                minVal = list1.val
                sorted = self.mergeTwoLists(list1.next,list2)

        return ListNode(minVal,sorted)

if __name__ == '__main__':
    s = Solution()
    # List1: [1,2,4]  List2: [1,3,4]
    # Expected: [1,1,2,3,4,4] 
    ans = s.mergeTwoLists(ListNode(1,ListNode(2,ListNode(4,None))), ListNode(1,ListNode(3,ListNode(4,None))))
    while ans:
        print(ans.val, end=" ")
        ans = ans.next
