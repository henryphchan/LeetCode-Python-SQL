# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ptrS = 0
        ptrT = 0
        while ptrS < len(s) and ptrT < len(t):
            if s[ptrS] == t[ptrT]:
                ptrS += 1
            ptrT += 1
        if ptrS >= len(s):
            return True
        else:
            return False

if __name__ == "__main__":
    s = Solution()
    print(s.isSubsequence("abc","ahbgdc"))
    print(s.isSubsequence("axc","ahbgdc"))