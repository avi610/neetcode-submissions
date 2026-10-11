class Solution:
    def encode(self, strs: List[str]) -> str:
        encodedStrs = []
        for i in range(len(strs)):
            encodedStrs.append(''.join((str(len(strs[i])),'#', strs[i])))
        return ''.join(encodedStrs)
    
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            size = ''
            while i < len(s) and s[i] != '#':
                size += s[i]
                i += 1
            j = int(size)
            i += 1
            val = ''
            while i < len(s) and j > 0:
                val += s[i]
                i += 1
                j -= 1
            res.append(val)
        
        return res
