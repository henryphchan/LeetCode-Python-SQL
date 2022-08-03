# https://leetcode.com/problems/remove-palindromic-subsequences/
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]: 
            return 1
        else:
            return 2

if __name__ == '__main__':
    s = Solution()
    print(s.removePalindromeSub("ababa"))
    print(s.removePalindromeSub("abbbbb"))
    print(s.removePalindromeSub("baabb"))