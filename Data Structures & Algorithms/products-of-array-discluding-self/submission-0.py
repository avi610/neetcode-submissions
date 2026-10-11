class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lprod = [1 for num in nums]
        rprod = [1 for num in nums]

        for i in range(1, len(nums)):
            lprod[i] = lprod[i-1] * nums[i-1]
        
        for i in reversed(range(len(nums) - 1)):
            rprod[i] = rprod[i+1] * nums[i+1]

        for i in range(len(nums)):
            nums[i] = lprod[i] * rprod[i]

        return nums