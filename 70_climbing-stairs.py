# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        first = 1
        second = 2
        current = 0
        
        if n == 1: return first
        if n == 2: return second
        
        for i in range(3,n+1,1):
            current = first + second
            first = second
            second = current
            
        return current

if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(5))