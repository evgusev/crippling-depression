from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        c = Counter(s)
        c2 = Counter(t)
        c.subtract(c2)
        

        for word in c:
            if c[word] != 0:
                return False
        return True
    

s = Solution()
print(s.isAnagram("anagram", "nagaram"))
print(s.isAnagram("rat", "car"))