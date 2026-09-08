class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_bar = 0
        right_bar = len(heights)-1  
        max_container = (right_bar-left_bar)*(min(heights[right_bar],heights[left_bar]))

        while left_bar<right_bar:
            container = (right_bar-left_bar)*(min(heights[right_bar],heights[left_bar]))
            if heights[left_bar]<heights[right_bar]:
                left_bar+=1
            else:
                right_bar-=1
            if container > max_container:
                max_container = container
                

        return max_container