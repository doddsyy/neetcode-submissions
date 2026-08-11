class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]] +=1
            else:
                freq[nums[i]] = 1
        freq_map = {key: [] for key in range(len(nums) + 1)}

        for key,value in freq.items():
            freq_map[value].append(key)

        res = []
        for key in range(len(nums), -1, -1):
            for val in freq_map[key]:
                res.append(val)
                if len(res) == k:
                    return res


        