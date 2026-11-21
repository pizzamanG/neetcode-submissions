class TimeMap:

    def __init__(self):
        self.dic = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.dic:
            self.dic[key].append((timestamp,value))
        else:
            self.dic[key] = [(timestamp,value)]

        
    def get(self, key: str, timestamp: int) -> str:
        try:
            arr = self.dic[key]
        except:
            return ""
        

        l = 0 
        r = len(arr) -1
        res = ""
        while l <= r:
            mid = l + (r-l) //2
            if arr[mid][0] == timestamp:
                return arr[mid][1]
            elif arr[mid][0] < timestamp:
                res = arr[mid][1]
                l = mid +1
            elif arr[mid][0] > timestamp:
                r = mid -1
        return res
        


 



        
