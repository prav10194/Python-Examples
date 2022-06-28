class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        
        for index in range(len(intervals)):
            
            startTime = intervals[index][0]
            endTime = intervals[index][1]
            
            if newInterval[1] < startTime: 
                res.append(newInterval)
                return res + intervals[index:]
            
            elif endTime < newInterval[0]:
                res.append(intervals[index])
            
            else:
                newInterval = [min(startTime, newInterval[0]), max(endTime, newInterval[1])]
        
        res.append(newInterval)
            
        return res
