class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        srt = sorted(nums)
        result = []

        for i in range(len(srt)):
            if i > 0 and srt[i] == srt[i - 1]:
                continue

            target = -srt[i]
            left = i + 1
            right = len(srt) - 1

            while left < right:
                res = srt[left] + srt[right]

                if res < target:
                    left += 1

                elif res > target:
                    right -= 1

                else:
                    result.append([srt[i], srt[left], srt[right]])

                    left += 1
                    right -= 1

                    while left < right and srt[left] == srt[left - 1]:
                        left += 1

                    while left < right and srt[right] == srt[right + 1]:
                        right -= 1

        return result