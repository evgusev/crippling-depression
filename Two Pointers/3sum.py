from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Сначала сортируем массив, потом для каждого элемента > 0 ищем two-sum-ii-input-array-is-sorted
        result = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and num == nums[i - 1]:
                continue

            l = i+1
            r = len(nums) - 1
            while l < r:
                if (num + nums[l] + nums[r] > 0):
                    r -= 1
                elif (num + nums[l] + nums[r] < 0):
                    l += 1
                else:
                    result.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    #если след. элемент такой же как предыдущий - увеличиваем l что бы избежать дубликатов
                    while (nums[l] == nums[l-1] and l < r):
                        l += 1
        return result
    


s = Solution()
print (s.threeSum([-1,0,1,2,-1,-4]))
print (s.threeSum([0,1,1]))
print (s.threeSum([0,0,0]))
print (s.threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4,5,5,-10]))
