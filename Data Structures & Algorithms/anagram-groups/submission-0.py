class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sort each str in strs and strs --- seems time consuming -- O (n log n) + O (s log s)
        # if chars it can be 26 chars so convert each str into a []
        charCounter = defaultdict(list) # key [] => value []
        for i in range(len(strs)):
            curr = [0 for i in range(26)]
            for c in strs[i]:
                curr[ord(c)-ord('a')] += 1
            
            charCounter[tuple(curr)].append(i)

        res = []
        for anagram, values in charCounter.items():
            curr = []
            for v in values:
                curr.append(strs[v])
            res.append(curr)

        return res