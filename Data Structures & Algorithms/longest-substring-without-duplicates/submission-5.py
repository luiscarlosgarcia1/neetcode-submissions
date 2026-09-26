class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        res = 0
        ref = set()

        while r < len(s):
            if s[r] in ref:
                res = max(res, r - l)

                while s[l] != s[r]:
                    ref.discard(s[l])
                    l += 1

                l += 1

            ref.add(s[r])
            r += 1

        return max(res, r - l)