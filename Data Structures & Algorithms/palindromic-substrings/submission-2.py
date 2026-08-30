class Solution:
    def countSubstrings(self, s: str) -> int:
        sp = "^#" + "#".join(s) + "#$"

        n = len(sp)
        r = [0] * n

        center, right = 0, 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                r[i] = min(r[mirror], r[right - i])

            while sp[i + r[i] + 1] == sp[i - r[i] - 1]:
                r[i] += 1

            if r[i] >= r[center]:
                center = i
                right = i + r[i]

        print(sp, r)

        res = 0
        for i in range(len(r)):
            res += (r[i] + 1) // 2

        return res