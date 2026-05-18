class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        ref, res = defaultdict(int), 0

        for right in range(len(s)):
            ref[s[right]] += 1

            while (right - left + 1) - max(ref.values()) > k:
                ref[s[left]] -= 1
                left += 1
            
            res = max(res, (right - left + 1))

        return res