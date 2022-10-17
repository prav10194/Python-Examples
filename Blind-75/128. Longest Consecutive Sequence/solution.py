class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nSet = set(nums)
        maxLength = 0
        for num in nSet:
            if num - 1 not in nSet:
                tempLength = 0
                
                while (num + tempLength) in nSet:
                    tempLength += 1
                maxLength = max(maxLength, tempLength)
        return maxLength
                
        
                
