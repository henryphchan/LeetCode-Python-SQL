# https://leetcode.com/problems/same-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val != q.val:
            return False
        if self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right):
            return True
        return False

if __name__ == '__main__':
    s = Solution()
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)
    p.left.left = TreeNode(4)
    p.right.left = TreeNode(5)
    p.right.right = TreeNode(6)
    p.right.left.left = TreeNode(7)
    p.right.left.right = TreeNode(8)
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)
    q.left.left = TreeNode(4)
    q.right.left = TreeNode(5)
    q.right.right = TreeNode(6)
    q.right.left.left = TreeNode(7)
    q.right.left.right = TreeNode(8)
    print(s.isSameTree(p,q))