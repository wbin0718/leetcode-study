class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        
        graph = 0
        
        while right > left :
            
            graph = max(graph, min(height[left],height[right]) * (right - left))
            
            if height[left] < height[right]:
                left += 1
            else :
                right -= 1
        
        return graph
        
        