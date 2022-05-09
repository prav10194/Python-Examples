class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        area = 1
        while start <= end: 
            temp, start, end = (height[start], start, end - 1) if height[start] > height[end] else (height[end], start + 1, end)
            if temp*(end - start) > area:
                area = temp*(end - start)
        return area
