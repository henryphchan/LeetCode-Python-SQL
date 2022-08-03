# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
from typing import List

class Solution:
    # Two Pointers Solution
    # Time: O(n), Memory: O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]: 
        i = 0
        j = len(numbers) - 1
        while i <= j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i+1, j+1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1

# Binary Search Solution - Slower
    def binarySearch(self, numbers:List[int], target: int) -> int:
            low = 0
            high = len(numbers) - 1
            mid = 0
            while (high >= low):
                mid = (high + low) // 2
                if target > numbers[mid]:
                    low = mid + 1
                elif target < numbers[mid]:
                    high = mid - 1
                elif target == numbers[mid]:
                    return mid
            # Not found
            return -1 
        
    def twoSumBS(self, numbers: List[int], target: int) -> List[int]:        
        for i in range(len(numbers)):
            value = target - numbers[i]
            j = self.binarySearch(numbers[i+1:], target - numbers[i])
            if j != -1:
                return [i+1, j+i+2]

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2,7,11,15],9))
    print(s.twoSum([2,3,4],6))
    print(s.twoSum([3,3],6))
    print(s.twoSum([5,25,75],100))
    print(s.twoSumBS([2,7,11,15],9))
    print(s.twoSumBS([2,3,4],6))
    print(s.twoSumBS([3,3],6))
    print(s.twoSumBS([5,25,75],100))