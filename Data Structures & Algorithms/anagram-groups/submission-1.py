class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []

        s_copy = strs.copy()
        for i, s in enumerate(s_copy):
            s_copy[i] = ''.join(sorted(s))
        
        anagrams = set(s_copy)
        for a in anagrams:
            temp = []
            for i, s in enumerate(s_copy):
                if a == s:
                    temp.append(strs[i])
            sublists.append(temp)

        return sublists
