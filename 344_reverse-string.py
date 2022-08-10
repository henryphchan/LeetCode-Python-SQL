# https://leetcode.com/problems/reverse-string/
from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            t = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = t

if __name__ == '__main__':
    s = Solution()
    s.reverseString(['H','e','l','l','o'])