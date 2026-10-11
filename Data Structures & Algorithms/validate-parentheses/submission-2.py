from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        parenMap = {')':'(', '}':'{', ']':'['}
        seen = deque()
        for c in s:
            if c not in parenMap:
                seen.append(c)
            else:
                if not seen or seen.pop() != parenMap[c]:
                    return False
        return len(seen) == 0