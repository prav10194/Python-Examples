class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x:x[0])
        index = 0
        while index < len(intervals):
            if index < len(intervals) - 1 and intervals[index][1] >= intervals[index+1][0]:
                intervals[index+1] = [min(intervals[index][0], intervals[index+1][0]), max(intervals[index][1], intervals[index+1][1])]
                intervals.pop(index)
            else:
                index += 1
        return intervals
