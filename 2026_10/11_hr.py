class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        while left <= right:
            l_height = height[left]
            r_height = height[right]
            idx = right - left 
            small = min(l_height, r_height)
            
            if small * idx > water:
                water = small * idx
            if l_height > r_height:
                right -= 1
            else:
                left += 1
        return water
