class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = []
        checked = []

        for i in strs:
            temp = []

            target = sorted(i)
            if target in checked:
                continue
            else: 
                checked.append(target)

            for j in strs:
                comp = sorted(j)
                if target == comp:
                    temp.append(j)

            sublists.append(temp)

        return sublists