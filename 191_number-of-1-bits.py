# https://leetcode.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight(self, n: int) -> int:
        return f'{n:32b}'.count('1')
        
if __name__ == '__main__':
    s = Solution()
    print(s.hammingWeight("00000000000000000000000000001011"))