class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        ans = [[] for i in range(len(nums)+1)]
        for n, f in count.items():
            ans[f].append(n)

        res = []
        for sub in reversed(ans):
            for i in sub:
                res.append(i)
                if len(res) == k:
                    return res