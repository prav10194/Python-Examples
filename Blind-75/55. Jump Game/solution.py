class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        
        for index in range(len(nums) - 2, -1, -1):
            jump = nums[index]
            
            if (index + jump) >= goal:
                goal = index
        
        return (goal == 0)
        
