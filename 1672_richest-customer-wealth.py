# https://leetcode.com/problems/richest-customer-wealth/
from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        largest = 0
        for customer in accounts:
            customerAmount = sum(customer)
            if customerAmount > largest:
                largest = customerAmount
        return largest
                
if __name__ == "__main__":
    s = Solution()
    print(s.maximumWealth([[1,5],[7,3],[3,5]]))