from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1,-1):
            output[i] *= postfix
            postfix *= nums[i]

        return output

s = Solution()
print (s.productExceptSelf([1,2,3,4]))
print (s.productExceptSelf([-1,1,0,-3,3]))