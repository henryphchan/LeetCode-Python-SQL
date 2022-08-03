# https://leetcode.com/problems/pascals-triangle/
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pasTri = list()
        for level in range(numRows): # Loop each level
            row = []
            if level == 0:
                row = [1]
                pasTri.append(row)
            else:
                for num in range(level+1): # Cal. the values in each row
                    if num == 0 or num == level : row.append(1) # First and Last value in each row
                    elif num == 1 or num == level -1 : row.append(level) 
                    elif num > 1 :
                        row.append(pasTri[level-1][num-1]+pasTri[level-1][num])
                pasTri.append(row)
                    
        return pasTri

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))