class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res,l,r = 0,0,len(heights)-1

        while l < r:
            left, right = heights[l], heights[r]
            res=max(res, min(left,right) * (r-l))
            if left <= right:
                l += 1
            else:
                r -= 1

        return res