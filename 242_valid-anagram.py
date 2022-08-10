# https://leetcode.com/problems/valid-anagram/
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

if __name__ == '__main__':
    s = Solution()
    print(s.isAnagram('eat','ate'))
    print(s.isAnagram('car','bar'))