# https://leetcode.com/problems/longest-common-prefix/
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        for i in range(1,len(strs)):
            pos = 1
            while strs[i].startswith(ans[:pos]) and len(ans) >= pos:
                pos += 1
            ans = strs[i][:pos-1]

        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))
    print(s.longestCommonPrefix(["aaaaaaaaaaa"]))
    print(s.longestCommonPrefix(["aaaaaaaaaaa","aa"]))