# https://leetcode.com/problems/palindrome-number
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            lastHalf = 0
            
            while x > lastHalf:
                lastHalf = lastHalf * 10 + x % 10
                if x == lastHalf: return True
                x = x // 10
                
            if x == lastHalf: return True
            
if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(1231))
    print(s.isPalindrome(0))
    print(s.isPalindrome(-1))
    print(s.isPalindrome(9999))
    print(s.isPalindrome(10))