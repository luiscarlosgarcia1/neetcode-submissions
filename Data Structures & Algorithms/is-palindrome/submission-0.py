class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ''.join(c for c in s if c.isalnum())
        cleanS = cleanS.lower()
        return cleanS == cleanS[::-1]