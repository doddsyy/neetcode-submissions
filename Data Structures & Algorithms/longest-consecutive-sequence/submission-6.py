class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)

        max_count = 0
        
        for num in seen:
            if num-1 not in seen:
                start = num
                count = 0
                while start in seen:
                    count+=1
                    start+=1
                if count > max_count:
                    max_count = count
        return max_count
        


        