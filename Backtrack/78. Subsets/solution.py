class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        # storing all final subsets
        result = []
        
        # storing temporary subset
        subset = []
        
        def backtracking(index):
            if index >= len(nums):
                result.append(subset.copy()) # appending current copy of subset
                return
            
            subset.append(nums[index])
            backtracking(index+1)
            
            subset.pop()
            backtracking(index+1)
            
        backtracking(0)
        return result
        
