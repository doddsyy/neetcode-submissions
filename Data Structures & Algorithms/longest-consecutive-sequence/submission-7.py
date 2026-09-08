class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        largest = 0

        for num in nums:
            starter = num
            count = 1 
            if starter-1 not in seen:
                while starter in seen:
                    starter+=1
                    if starter not in seen:
                        break
                    count+=1
                if count > largest:
                    largest = count
                seen.add(num)
        return largest
                
            



        