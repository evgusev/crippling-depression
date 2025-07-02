import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = re.sub(r'[^a-zA-Z0-9]', '',  s).lower()
        for i in range(len(s2)):
            if (s2[i] != s2[len(s2)-i-1]):
                return False
        return True
    
    def isPalindromeTwoPointers(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True
    
    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
        

s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome(" "))
print(s.isPalindrome("0P"))

print("- - -")

print(s.isPalindromeTwoPointers("A man, a plan, a canal: Panama"))
print(s.isPalindromeTwoPointers("race a car"))
print(s.isPalindromeTwoPointers(" "))
print(s.isPalindromeTwoPointers("0P"))
