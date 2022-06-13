# https://leetcode.com/problems/triangle/

from typing import List
class Solution:
    # Top-down Approach
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        accSum = [] # accumunated path sum of the triangle
        for i in range(len(triangle)):
            newRow = []
            if i == 0:
                newRow.append(triangle[0][0])
            if i > 0:
                for j in range(len(triangle[i])):
                    if j == 0: 
                        newRow.append(accSum[i-1][j]+triangle[i][j])
                    elif j >= i:
                        newRow.append(accSum[i-1][j-1]+triangle[i][j])
                    else:
                        newRow.append(min(accSum[i-1][j-1],accSum[i-1][j])+triangle[i][j])
            accSum.append(newRow)
        
        return min(accSum[-1])

if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
    print(s.minimumTotal([[2],[3,4],[7,6,5],[4,1,8,3]]))
    print(s.minimumTotal([[2],[3,4],[999,999,5],[4,1,8,3]]))