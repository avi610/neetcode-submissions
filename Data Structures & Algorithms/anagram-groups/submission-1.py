
class Solution:
    def parseString(self, s: str):
        charMap = [0] * 26
        for c in s:
            charMap[ord(c) - ord('a')] += 1
        return tuple(charMap)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for s in strs:
            parsedS = self.parseString(s)
            if parsedS in seen:
                seen[parsedS].append(s)
            else:
                seen[parsedS] = [s]
        sol = []
        for s in seen:
            sol.append(seen[s])

        return sol