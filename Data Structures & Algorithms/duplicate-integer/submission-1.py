class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = {}
        for i in range(len(nums)):
            if nums[i] in tracker:
                return True
            tracker[nums[i]] = i
        return False

        