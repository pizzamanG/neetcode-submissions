"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        arr = sorted(intervals, key=lambda x: x.end)

        end = arr[0].end

        for i in range(1,len(arr)):
            new_start, new_end = arr[i].start, arr[i].end
            if new_start < end:
                return False
            end = new_end
        return True
            



