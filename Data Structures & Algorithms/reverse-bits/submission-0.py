class Solution:
    def reverseBits(self, n: int) -> int:
        shift = 31
        res = 0
        while n:
            if n & 1:
                res |= 1 << shift
            shift -= 1
            n >>= 1
        return res