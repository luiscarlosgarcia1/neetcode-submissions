from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res = 0
        Q = deque([0])
        dp = set()

        while Q:
            for _ in range(len(Q)):
                cur = Q.popleft()
                if cur == amount:
                    return res
                if cur >= amount:
                    continue

                for c in coins:
                    if cur + c in dp:
                        continue
                    Q.append(cur + c)
                    dp.add(cur + c)

            res += 1

        return -1