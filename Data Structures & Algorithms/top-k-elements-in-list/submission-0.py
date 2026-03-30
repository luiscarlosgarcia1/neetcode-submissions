class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        temp = []
        for key in freq:
            temp.append((freq[key], key))
        temp = sorted(temp, reverse=True)

        res = []
        for i in range(k):
            res.append(temp[i][1])
        
        return res