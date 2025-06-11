
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = {}
        s = 'duplicate'
        for num in nums:
            if num in d and d[num] == s:
                return True
            else:
                d[num] = s
        return False
    

s = Solution()
print (s.containsDuplicate([1,2,3,1]))
print (s.containsDuplicate([1,2,3,4]))
print (s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))