class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        areas = []
        
        while (left < right):
            minHeight = min(height[left], height[right])
            area = (right - left) * minHeight
            
            if (height[left] <= height[right]):
                left += 1
            else:
                right -= 1
                
            areas.append(area)
            
        return max(areas)