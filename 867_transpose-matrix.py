# https://leetcode.com/problems/transpose-matrix/
from typing import List
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j >= len(ans):
                    ans.append([matrix[i][j]])
                else:
                    ans[j].append(matrix[i][j])
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.transpose([[1,2,3],[4,5,6],[7,8,9]]))