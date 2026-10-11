class Solution:
    def findMin(self, nums: List[int]) -> int:
        # need to account for pivot
        # if nums[l] < nums[m] < nums[hi] then no rotation
        # if nums[l] < nums[m] > nums[hi] then min on right
        # if nums[l] > nums[m] < nums[hi] then min on left
        l, h = 0, len(nums) - 1

        while l < h:
            m = (h-l)//2 + l
            if nums[l] < nums[m] and nums[m] < nums[h]:
                return nums[l]
            elif nums[m] > nums[h]:
                l = m + 1
            else:
                h = m

        return nums[l]