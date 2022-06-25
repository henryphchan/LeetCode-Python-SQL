# https://leetcode.com/problems/running-sum-of-1d-array/
from typing import List
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            if i == 0:
                answer.append(nums[i])
            else:
                answer.append(nums[i] + answer[i-1])
        return answer

if __name__ == "__main__":
    s = Solution()
    print(s.runningSum([1,2,3,5]))