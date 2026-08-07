class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker = {}
        for i, num in enumerate(nums):
            if target-nums[i] in tracker:
                return [tracker[target-nums[i]],i]
            tracker[nums[i]] = i
            