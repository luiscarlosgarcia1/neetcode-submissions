class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanS = ''.join(c.lower() for c in s if c.isalnum())
        return cleanS == cleanS[::-1]

        # could have better time and space complexity