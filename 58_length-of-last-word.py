# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))