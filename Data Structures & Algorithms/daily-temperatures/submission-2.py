from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        res = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack:
                # no previous days
                stack.append(i)
            elif temperatures[stack[-1]] < temp:
                # resolve all days in stack whose warmer day is today
                while stack and temperatures[stack[-1]] < temp:
                    res[stack[-1]] = i - stack[-1]
                    stack.pop()
                stack.append(i)
            else:
                stack.append(i)

        return res
