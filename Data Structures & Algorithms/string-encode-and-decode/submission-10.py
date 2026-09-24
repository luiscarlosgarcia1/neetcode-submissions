class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s

        print(res)

        return res

    def decode(self, s: str):
        res = []
        
        part = i = 0
        while i < len(s):
            i += 1

            if s[i] != "#":
                continue

            size = int(''.join(s[part:i]))
            part, i = i + 1, i + size + 1
            res.append(s[part:i])
            part = i

        return res