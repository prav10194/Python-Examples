class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      
        results = []
    
        tempSubset = []
        
        def bt(i, tempSum):
            if tempSum == target:
                results.append(tempSubset.copy())
                return
            
            if tempSum > target or i >= len(candidates):
                return 
            
            tempSubset.append(candidates[i])
            tempSum += candidates[i]
            bt(i, tempSum)
            
            tempSubset.pop()
            tempSum -= candidates[i]
            bt(i + 1, tempSum)
            
        bt(0, 0)
        return results
        
