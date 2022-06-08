# https://leetcode.com/problems/two-sum/
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - value
            
            if remaining in seen:
                return [i,seen[remaining]]
            else:
                seen[value]=i

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
    print(s.twoSum([3,2,4],6))
    print(s.twoSum([3,3],6))
