"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals = sorted(intervals, key = lambda x : x.start)
        import heapq
        h = []
        rooms = 0
        for meeting in intervals:
            start, end = meeting.start, meeting.end

            if h and h[0] <= start:

                heapq.heappop(h)
            elif (not h) or h[0] > start:
                rooms +=1

            heapq.heappush(h, end)
        return rooms


      
    








        