class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sol = {}
        for num in nums:
            sol[num] = 1
        maxSoFar = 0
        for i in range(len(nums)):
            if nums[i]-1 not in sol:
                j = 1
                while (nums[i] + j) in sol:
                    j += 1
                maxSoFar = max(maxSoFar, j)
        return maxSoFar