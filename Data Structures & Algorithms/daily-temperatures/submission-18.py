class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ts = temperatures
        results = [0] * len(ts)
        stack = []
        for i in range(len(ts)):
            temp = ts[i]
            while stack and temp > ts[stack[-1]]:
                day = stack.pop()
                results[day] = i - day
            stack.append(i)
        return results       


    
         







   