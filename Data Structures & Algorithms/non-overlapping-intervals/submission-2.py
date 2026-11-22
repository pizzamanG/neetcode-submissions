class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = sorted(intervals, key = lambda x : x[1])
        count = 0

        end = arr[0][1]

        for i in range(1,len(arr)):
            start = arr[i][0]
            if start < end:
                count +=1
            elif start >= end:
                end = arr[i][1]
        return count

          


        