class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        N = len(nums[0])
        strSet = { s for s in nums }
        
        def backtrack(index, binStr):
            if index == N:
                if binStr not in strSet:
                    return binStr
                else:
                    return None
            
            return (backtrack(index + 1, binStr + "0") or backtrack(index + 1, binStr + "1"))
        
        return backtrack(0, '')
        
        
        
        
