from collections import deque

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = deque()

        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                ans = max(ans, height * width)
            stack.append(i)

        return ans