from collections import defaultdict
from typing import Counter, List


class Solution:
    def groupAnagramsSlow(self, strs: List[str]) -> List[List[str]]:
        output = []

        for word in strs[1:]:
            anagramFound = False
            for outputGroup in output:
                print(word, outputGroup)
                if (len(word) != len(outputGroup[0])):
                    continue
                if self.__isAnagram(word, outputGroup[0]):
                    outputGroup.append(word)
                    anagramFound = True
                    break
            if not anagramFound:
                output.append([word])

        return output

    def __isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        c = Counter(s)
        c2 = Counter(t)
        c.subtract(c2)
        

        for word in c:
            if c[word] != 0:
                return False
        return True
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        current = ord('a')
        finish = ord('z')
        dCounter = dict()
        while current <= finish:
            dCounter[current] = 0
            current += 1

        for s in strs:
            d = dCounter.copy()
            for c in s:
                d[ord(c)] += 1

            result[tuple(d.items())].append(s)

        return list(result.values())
    
    def groupAnagramsPirated(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
            
            
s = Solution()
# print (s.groupAnagramsSlow(["eat","tea","tan","ate","nat","bat"]))
# print (s.groupAnagramsSlow([""]))
# print (s.groupAnagramsSlow(["a"]))

print (s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print (s.groupAnagrams([""]))
print (s.groupAnagrams(["a"]))

# print (s.groupAnagramsPirated(["eat","tea","tan","ate","nat","bat"]))
# print (s.groupAnagramsPirated([""]))
# print (s.groupAnagramsPirated(["a"]))
