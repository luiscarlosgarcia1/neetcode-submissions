class Solution:
    def numDecodings(self, s: str) -> int:
        one, two = 1, 0

        for i in range(len(s) - 1, -1 , -1):
            cur = 0

            if s[i] != "0":
                cur += one
            
                if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                    cur += two

            two, one = one, cur

        return one