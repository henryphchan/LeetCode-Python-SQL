# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for i in range(len(s)):
            if ord(s[i]) >= 65 and ord(s[i]) <= 90:
                newStr += chr(ord(s[i]) + 32)
            elif (ord(s[i]) >= 97 and ord(s[i]) <= 122) or (ord(s[i]) >= 48 and ord(s[i]) <= 57):
                newStr += s[i]
        return newStr == newStr[::-1]

if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
    print(s.isPalindrome("race a car"))
    print(s.isPalindrome("0P"))
    print(s.isPalindrome(" "))
    