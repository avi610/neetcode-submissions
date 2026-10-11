from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)
        for c in s:
            seen[c] += 1
        for c in t:
            seen[c] -= 1
        
        for key, val in seen.items():
            if seen[key] != 0:
                return False
        return True    