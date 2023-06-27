#https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        if num % 10 == num:
            return num
        else:
            return self.addDigits(self.addDigits(num//10) + num%10)

if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(38))
    print(s.addDigits(123))
    print(s.addDigits(9999))
    print(s.addDigits(0))