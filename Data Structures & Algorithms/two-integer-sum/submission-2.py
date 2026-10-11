class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rem = {}
        for i in range(len(nums)):
            wanted = target - nums[i]
            if wanted in rem:
                return [rem[wanted], i]
            else:
                rem[nums[i]] = i

        return []
