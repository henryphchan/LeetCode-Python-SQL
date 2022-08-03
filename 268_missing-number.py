# https://leetcode.com/problems/missing-number/
from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int(((len(nums)+1)/2)*(len(nums)) - sum(nums))

if __name__ == '__main__':
    s = Solution()
    print(s.missingNumber([9,6,4,2,3,5,7,0,1]))