
from collections import defaultdict
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for num, cnt in d.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

s = Solution()
print (s.topKFrequent([1,1,1,1,1,2,2,3], 2))
print (s.topKFrequent([1], 1))
