# https://leetcode.com/problems/contains-duplicate-ii/
from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for idx,val in enumerate(nums):
            if val not in seen:
                seen[val] = idx
            elif idx - seen[val] <= k:
                return True
            else:
                seen[val] = idx
        return False

if __name__ == "__main__":
    s = Solution()
    print(s.containsNearbyDuplicate([1,0,1,1],1))
    print(s.containsNearbyDuplicate([1,2,3,1],3))