class Solution:

    def encode(self, strs: List[str]) -> str:
        single = ''
        for s in strs:
            s += ';'
            single += s
        return single
    def decode(self, s: str) -> List[str]:
        temp = ''
        res = []
        for i in range(len(s)):
            if s[i] != ';':
                temp += s[i]
            else:
                res.append(temp)
                temp = ''
        return res