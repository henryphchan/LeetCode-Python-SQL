# https://leetcode.com/problems/pascals-triangle-ii/

from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = list()
        for r in range(rowIndex+1):
            if r == 0: 
                value = 1
            else:
                value = result[-1] * (rowIndex - r + 1) / r # new value = prev value * (n-r+1) / r
            result.append(int(value))
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(0))
    print(s.getRow(1))
    print(s.getRow(2))
    print(s.getRow(3))
    print(s.getRow(4))
    print(s.getRow(5))
    print(s.getRow(33))