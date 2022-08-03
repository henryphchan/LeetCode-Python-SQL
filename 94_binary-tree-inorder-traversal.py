# https://leetcode.com/problems/binary-tree-inorder-traversal/
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
# Recursive Approach
#        if tn is None:
#            return list()
#        l = self.inorderTraversal(tn.left) 
#        l.append(tn.val)
#        l.extend(self.inorderTraversal(tn.right))
#        return l

# Iterative Approach
        if root is None:
            return list()
        
        stack = []
        result = []
        node = root
        
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                result.append(node.val)
                node = node.right
                
        return result
                
if __name__ == '__main__':
    s = Solution()
    tn = TreeNode(1)
    tn.left = TreeNode(2)
    tn.right = TreeNode(3)
    tn.left.left = TreeNode(4)
    tn.right.left = TreeNode(5)
    tn.right.right = TreeNode(6)
    tn.right.left.left = TreeNode(7)
    tn.right.left.right = TreeNode(8)
    print(s.inorderTraversal(tn))