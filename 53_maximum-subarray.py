# https://leetcode.com/problems/maximum-subarray/
from typing import List
import sys

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = -sys.maxsize - 1
        for num in nums:
            curSum += num
            
            if curSum > maxSum:
                maxSum = curSum
            
            if curSum < 0:
                curSum = 0
        
        return maxSum

if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
    print(s.maxSubArray([-1]))