class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = [-1, -1]
        tcount, scount = defaultdict(int), defaultdict(int)

        for c in t:
            tcount[c] += 1
        have, need = 0, len(tcount)

        l = 0
        for r in range(len(s)):
            if s[r] in tcount:
                scount[s[r]] += 1
                if scount[s[r]] == tcount[s[r]]:
                    have += 1

            while have == need: # valid window
                #update res
                if r - l + 1 < res[1] - res[0] or res == [-1, -1]:
                    res = [l, r + 1]
                #shrink window
                if s[l] in scount:
                    scount[s[l]] -= 1
                    if scount[s[l]] < tcount[s[l]]:
                        have -= 1
                l += 1

        return "" if res[0] == -1 else s[res[0]:res[1]]