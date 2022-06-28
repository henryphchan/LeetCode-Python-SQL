# https://leetcode.com/problems/plus-one/
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        pos = len(digits) - 1
        while carry > 0:
            if digits[pos] == 9:
                digits[pos] = 0
                if pos > 0:
                    carry = 1
                    pos -= 1
                else:
                    carry = 0
                    digits.insert(0,1)
            else:
                digits[pos] += 1
                carry = 0
                
        return digits
                
if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([4,3,2,1]))
    print(s.plusOne([9,9,9,9]))