# https://leetcode.com/problems/implement-strstr

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        pos = 0
        i = 0
        
        if len(needle) == 0:
            return 0
        
        while i < len(haystack):
            if haystack[i] == needle[pos]:
                pos += 1
            else:
                i = i - pos
                pos = 0
            if pos > len(needle) - 1:
                return i - pos + 1
            i += 1
        
        return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("hello","ll"))
    print(s.strStr("aaaaa","baa"))
    print(s.strStr("hello",""))