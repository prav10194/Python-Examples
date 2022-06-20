class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        
        perimeter = sum(matchsticks)
        sides = [0] * 4
        
        if perimeter % 4 != 0:
            return False
        
        maxLength = perimeter // 4
        
        matchsticks.sort(reverse=True)
        
        if matchsticks[0] > maxLength:
            return False
        
        def backtrack(index):
            if index == len(matchsticks):
                return True
            
            for j in range(4):
                if sides[j] + matchsticks[index] <= maxLength: 
                    sides[j] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[j] -= matchsticks[index]
            return False
        
        return backtrack(0)
            
            
            
        
