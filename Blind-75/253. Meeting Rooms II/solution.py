class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        startIntervals = sorted([x[0] for x in intervals])
        endIntervals = sorted([x[1] for x in intervals])
        
        startIndex, endIndex = 0, 0
        rooms, maxRooms = 0, 0
        
        while startIndex < len(startIntervals) and endIndex < len(startIntervals):
            if startIntervals[startIndex] < endIntervals[endIndex]:
                startIndex += 1
                rooms += 1
                maxRooms = max(maxRooms, rooms)
            else:
                endIndex += 1
                rooms -= 1
                maxRooms = max(maxRooms, rooms)
        return maxRooms
        
        
