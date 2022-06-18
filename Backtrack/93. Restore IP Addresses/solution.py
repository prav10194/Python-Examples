class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        result = []
        
        if len(s) < 4 and len(s) > 12:
            return result
        
        def backtrack(index, dots, validIP):
            if dots == 4 and index == len(s):
                result.append(validIP[:-1])
                return
            
            if dots > 4:
                return
            
            for strIndex in range(index, min(index+3, len(s))):
                if int(s[index:strIndex+1]) < 256 and (strIndex == index or s[index]!="0"):
                    backtrack(strIndex + 1, dots + 1, validIP + s[index:strIndex+1] + ".")
                    
        backtrack(0, 0, "")
        return result
        
