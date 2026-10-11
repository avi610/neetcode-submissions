class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL, maxR = [0] * n, [0] * n

        for i in range(1, n):
            maxL[i] = max(maxL[i], height[i-1], maxL[i-1])

        for i in reversed(range(0, n-1)):
            maxR[i] = max(maxR[i], height[i+1], maxR[i+1])

        print(maxL)
        print(maxR)
        ans = 0
        for i, h in enumerate(height):
            ans += max(min(maxL[i], maxR[i]) - h,0)

        return ans