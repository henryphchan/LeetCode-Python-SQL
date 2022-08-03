# https://leetcode.com/problems/symmetric-tree/
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isMirror(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        if p.val != q.val:
            return False
        if self.isMirror(p.left, q.right) and self.isMirror(p.right, q.left):
            return True
        return False
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirror(root, root)

if __name__ == '__main__':
    s = Solution()
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.right = TreeNode(2)
    tn.left.left = TreeNode(3)
    tn.right.right = TreeNode(3)
    print(s.isSymmetric(tn))