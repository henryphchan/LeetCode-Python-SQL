# https://leetcode.com/problems/search-insert-position/
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        high = len(nums) - 1
        low = 0
        mid = 0
        
        if target > nums[len(nums)-1]: 
            return len(nums)
        elif target < nums[0]:
            return 0
        
        while low <= high:
            mid = (high + low) // 2
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                return mid
        
        if nums[mid] > target:
            if nums[mid - 1] < target:
                return mid
            return mid -1
        return mid + 1

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,6],4))
    print(s.searchInsert([1,3,5,6],2))