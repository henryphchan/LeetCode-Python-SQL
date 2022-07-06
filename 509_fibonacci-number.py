# https://leetcode.com/problems/fibonacci-number/
class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n == 0: return first
        if n == 1: return second
        for i in range(n-1):
            current = first + second 
            first = second
            second = current
        return current
            
if __name__ == '__main__':
    s = Solution()
    print(s.fib(2))
    print(s.fib(20))