class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        buckets = [[] for l in range(len(nums) + 1)]
        for key in freq:
            buckets[freq[key]].append(key)

        res = []
        for i in range(len(nums), 0, -1):
            for j in buckets[i]:
                res.append(j)
                if len(res) == k:
                    return res