class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        tracker = set()
        for i in range(len(nums)):
            if nums[i] in tracker:
                return True
            tracker.add(nums[i])
        return False

        