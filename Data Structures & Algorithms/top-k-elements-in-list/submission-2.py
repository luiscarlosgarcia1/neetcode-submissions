class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]
        res = []
        for n in nums:
            freq[n] += 1
        for key, value in freq.items():
            buckets[value].append(key)
        for i in range(len(buckets)-1, 0, -1):
            for item in buckets[i]:
                res.append(item)
                if (len(res) == k):
                    return res