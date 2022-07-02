# https://leetcode.com/problems/longest-palindrome/
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        charMap = Counter(s)
        longest = 0
        for i in charMap.values():
            longest += i // 2 * 2
        if sum(charMap.values()) - longest > 0:
            longest += 1
        return longest

if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("abccccdd"))
    print(s.longestPalindrome("ccc"))

