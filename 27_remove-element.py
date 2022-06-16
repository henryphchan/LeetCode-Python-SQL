# https://leetcode.com/problems/remove-element/
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        pos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[pos] = nums[i]
                pos += 1
        return pos
                
if __name__ == '__main__':
    s = Solution()
    arr = [0,1,2,2,3,0,4,2]
    print(s.removeElement(arr,2), end=" ")
    print(arr, end=" ")