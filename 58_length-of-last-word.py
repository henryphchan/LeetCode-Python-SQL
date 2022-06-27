# https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = 0
        for c in reversed(s.rstrip()):
            if c == ' ':
                return i
            else:
                i += 1
        return i

if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLastWord("Hello World"))