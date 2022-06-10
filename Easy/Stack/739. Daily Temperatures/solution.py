class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        
        for index in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[index]:
                i, t = stack.pop()
                res[i] = (index - i)
            stack.append([index, temperatures[index]])
        return res
        
