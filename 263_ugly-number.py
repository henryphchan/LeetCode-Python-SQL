#https://leetcode.com/problems/ugly-number/
class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0: return False
        if n in [1,2,3,5]: return True
        if n%2 == 0:
            return self.isUgly(n//2)
        elif n%3 == 0:
            return self.isUgly(n//3)
        elif n%5 == 0:
            return self.isUgly(n//5)
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isUgly(2))
    print(s.isUgly(6))
    print(s.isUgly(1))
    print(s.isUgly(14))
    print(s.isUgly(9))