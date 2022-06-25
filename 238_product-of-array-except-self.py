# https://leetcode.com/problems/product-of-array-except-self/
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        # Prefix
        for i in range(len(nums)):
            if i == 0:
                answer.append(1)
            else:
                answer.append(answer[i-1] * nums[i-1]) 
        #Postfix
        multi = 1
        for i in range(len(nums)-2,-1,-1):
            multi *= nums[i+1]
            answer[i] *= multi
        
        return answer

if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))
    print(s.productExceptSelf([-1,1,0,-3,3]))