# https://leetcode.com/problems/intersection-of-two-arrays/
from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = dict()
        intersection = list()
        for n in nums1:
            seen[n] = 0
        for n in nums2:
            if n in seen:
                seen[n] += 1
        for idx,val in seen.items():
            if val > 0:
                intersection.append(idx)
        return intersection

if __name__ == '__main__':
    s = Solution()
    print(s.intersection([4,9,5],[9,4,9,8,4]))