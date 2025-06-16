from typing import List


class Solution:
    # def longestConsecutive(self, nums: List[int]) -> int:
    #     seq = dict()

    #     maxCount = 0
    #     for num in nums:
    #         if not num in seq:
    #             seq[num] = num + 1

    #     for k in seq.keys():
    #         count = 0
    #         top = False
    #         j = k
    #         while not top:
    #             count += 1
    #             if (seq[j] in seq):
    #                 j += 1
    #             else:
    #                 top = True

    #         if (count > maxCount):
    #             maxCount = count

    #     return maxCount


    #optimal
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest


s = Solution()
print(s.longestConsecutive([100,4,200,1,3,2]))
print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(s.longestConsecutive([1,0,1,2]))