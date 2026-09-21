class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = defaultdict(int)

        for n in nums:
            ref[n] += 1

        ref = sorted(ref.items(), key=lambda x: x[1], reverse=True)

        return [ref[k][0] for k in range(0, k, 1)]