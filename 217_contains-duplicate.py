# https://leetcode.com/problems/contains-duplicate/
from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if seen.get(num) == 1:
                return True
            else:
                seen.update({num:1})
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(s.containsDuplicate([1,2,3,4]))