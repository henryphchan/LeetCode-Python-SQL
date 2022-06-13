# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pos = 0
        for i in range(len(nums)):
            if nums[i] > nums[pos]:
                pos += 1
                nums[pos] = nums[i]
        return pos+1

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))