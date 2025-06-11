from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            else:
                d[target - num] = i
        return []

            





s = Solution()
print (s.twoSum([2,7,11,15], 9))
print (s.twoSum([3,2,4], 6))
print (s.twoSum([3,3], 6))