class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        sum = nums[0]
        
        for index in range(1, len(nums)):
            dp.append(max(dp[index-1]+nums[index], nums[index]))
            
            if dp[index] > sum:
                sum = dp[index]
        return sum
        
