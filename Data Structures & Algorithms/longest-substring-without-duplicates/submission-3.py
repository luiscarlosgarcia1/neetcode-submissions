class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l, r = 0, 1
        res = 1 
        ref = {s[l]}

        while r < len(s):
            if s[r] in ref:
                res = max(res, len(ref))
                while s[l] != s[r]:
                    ref.discard(s[l])
                    l += 1
                l += 1
            else:
                ref.add(s[r])

            r += 1

        return max(res, len(ref))