class Solution:
    def longestPalindrome(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j + 1 <= 2 or dp[i - 1][j + 1]):
                    dp[i][j] = True
                    curLen = i - j + 1
                    if resLen < curLen:
                        resIdx = j
                        resLen = curLen

        return s[resIdx : resIdx + resLen]