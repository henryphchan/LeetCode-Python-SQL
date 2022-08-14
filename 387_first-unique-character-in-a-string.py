# https://leetcode.com/problems/first-unique-character-in-a-string/
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for idx,char in enumerate(s):
            if count[char] == 1:
                return idx
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.firstUniqChar('leetcode'))
    print(s.firstUniqChar('loveleetcode'))