from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))
            sublists[key].append(s)

        return list(sublists.values())