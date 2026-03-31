class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            comp = numbers[l] + numbers[r]
            if comp == target:
                return [min(l, r)+1, max(l, r)+1]
            elif comp < target:
                l += 1
            else:
                r -= 1
