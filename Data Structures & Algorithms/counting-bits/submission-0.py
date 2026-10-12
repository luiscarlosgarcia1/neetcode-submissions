class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [i for i in range(n + 1)]

        for i in range(len(res)):
            res[i] = bin(res[i]).count('1')

        return res