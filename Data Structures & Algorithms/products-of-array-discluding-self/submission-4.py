class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sum_arr = []

        left_prod = []
        right_prod = []
        
        left_count = 1
        right_count = 1

        length = len(nums)

        for i in range(length):
            left_prod.append(left_count)
            left_count *= nums[i]

        for i in range(length-1, -1, -1):
            right_prod.append(right_count)
            right_count *= nums[i]

        for i in range(length):
            sum_arr.append(left_prod[i] * right_prod[length -i-1])

        return sum_arr


        