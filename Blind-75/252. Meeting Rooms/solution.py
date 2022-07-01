class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x:x[0])
        if not intervals:
            return True
        prevEnd = intervals[0][1]
        
        for start, end in intervals[1:]: 
            if start < prevEnd:
                return False
            else:
                prevEnd = max(prevEnd, end)
        return True
