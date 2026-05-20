class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        c1, c2 = defaultdict(int), defaultdict(int)

        for c in s1:
            c1[c] += 1

        left = 0
        for right in range(len(s2)):
            c2[s2[right]] += 1
            
            if right < len(s1) - 1:
                continue
    
            if c1 == c2:
                return True

            c2[s2[left]] -= 1

            if c2[s2[left]] == 0:
                c2.pop(s2[left])
                
            left += 1

        return False