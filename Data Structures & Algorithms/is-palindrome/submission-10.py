class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() == s[r].lower():
                l += 1 
                r -= 1
            else:
                return False
        return True

    def isalnum(self, s: str) -> bool:
        return ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('a') or ord('0') <= ord(s) <= ord('9')
    def islower(self, s: str) -> str:
        if ord('a') <= ord(s) <= ord('a'):
            return s
        else:
            return str(ord(s) + 32)


        