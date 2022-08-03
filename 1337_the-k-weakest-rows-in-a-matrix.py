# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        sort = []
        for i in range(len(mat)):
            if len(sort)==0:
                sort.insert(1,i)
            else:
                for j in range(len(sort)):
                    if sum(mat[sort[j]]) > sum(mat[i]):
                        sort.insert(j,i)
                        break
                    elif j == len(sort)-1:
                        sort.append(i)
                        break
        return sort[:k]
            
if __name__ == '__main__':
    s = Solution()
    print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]],3))