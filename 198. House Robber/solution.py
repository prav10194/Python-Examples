class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_p2, rob_p1 = 0, 0
        temp_sum = 0
        
        for num in nums: 
            temp_sum = max(num + rob_p2, rob_p1)
            rob_p2 = rob_p1
            rob_p1 = temp_sum
        return temp_sum
