class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1

        ans = []
        for n, f in count.items():
            ans.append([f, n])

        ans.sort()

        return [ans.pop()[1] for i in range(k)]