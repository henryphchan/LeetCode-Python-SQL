# https://leetcode.com/problems/majority-element/
from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

if __name__ == '__main__':
    s = Solution()
    print(s.majorityElement([2,2,1,1,1,2,2]))