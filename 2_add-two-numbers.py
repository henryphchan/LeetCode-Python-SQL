# https://leetcode.com/problems/add-two-numbers/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:  
    def cal(self, rl1: ListNode, rl2: ListNode, result: ListNode, carry: int) -> Optional[ListNode]:
        newNode = rl1.val+rl2.val+carry
        if newNode > 9:
            newNode = newNode % 10
            carry = 1
        else:
            carry = 0
            
        if rl1.next == None and rl2.next == None and carry == 0:
            return ListNode(newNode,None)
        elif rl1.next == None and rl2.next == None and carry != 0:
            return ListNode(newNode,self.cal(ListNode(0,None), ListNode(0,None), result, carry))
        elif rl1.next == None:
            return ListNode(newNode,self.cal(ListNode(0,None), rl2.next, result, carry))
        elif rl2.next == None:
            return ListNode(newNode,self.cal(rl1.next, ListNode(0,None), result, carry))
        else:
            return ListNode(newNode,self.cal(rl1.next, rl2.next, result, carry))
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tempResult = ListNode()
        return self.cal(l1, l2, tempResult, 0)

if __name__ == '__main__':            
    s1 = Solution().addTwoNumbers(ListNode(2,ListNode(4,ListNode(3,None))),ListNode(5,ListNode(6,ListNode(4,None))))
    while s1:
        print(s1.val)
        s1 = s1.next