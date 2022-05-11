 class Solution:
    def trap(self, height: List[int]) -> int:   
        ans = 0
        for i in range(0, len(height)):
            left = 0
            right = 0
            for j in range(0, i+1):
                left = max(left, height[j])
            for j in range(i, len(height)):
                right = max(right, height[j])
            ans = ans + min(left, right) - height[i]
