class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals, key = lambda x : x[0])

        start = arr[0][0]
        end = arr[0][1]

        new_list = []
        for i in range(1,len(arr)):

            new_start = arr[i][0]
            new_end = arr[i][1]

            if new_start <= end:
                end = max(end, new_end)
                continue
                

            elif new_start > end:
            
                new_list.append([start,end])
                start = new_start
                end = new_end
        
        new_list.append([start,end])
        
        return new_list

            
             


        