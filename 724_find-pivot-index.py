# https://leetcode.com/problems/find-pivot-index/
from typing import List
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        for i in range(len(nums)):
            right -= nums[i]
            if left == right:
                return i
            left += nums[i]
            #print(i,':',left,right)

        return -1

if __name__ == "__main__":
    s = Solution()
    print(s.pivotIndex([1,1,1,1,1]))
    print(s.pivotIndex([0,0,0,0]))
    print(s.pivotIndex([-1,-1,-1,-1,-1,0]))
    print(s.pivotIndex([-1,-1,-1,1,1,1]))
    print(s.pivotIndex([1,-1,-1,-2,1,1,1,1]))
    print(s.pivotIndex([-1,-1,0,0,-1,-1]))