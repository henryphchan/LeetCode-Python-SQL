# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        unhappy = set()
        cur = n
        while True:
            if cur in unhappy: return False
            unhappy.add(cur)
            nex = 0
            while cur != 0:
                nex = nex + pow(cur % 10, 2)
                cur = cur // 10
            if nex == 1: return True
            cur = nex

if __name__ == '__main__':
    s = Solution()
    print(s.isHappy(19))
    print(s.isHappy(2))