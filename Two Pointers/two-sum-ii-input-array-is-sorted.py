from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # т.к. массив отсортирован идем с разных концов массива, в итоге найдем искомое число.
        l = 0
        r = len(numbers)-1
        
        while l < r:
            if (numbers[l] + numbers[r] == target):
                return [l+1, r+1]
            if (numbers[l] + numbers[r] > target):
                r -= 1
            if (numbers[l] + numbers[r] < target):
                l +=1

s = Solution()
print (s.twoSum([2,7,11,15], 9))
print (s.twoSum([2,3,4], 6))
print (s.twoSum([-1,0], -1))
print (s.twoSum([5,25,75], 100))