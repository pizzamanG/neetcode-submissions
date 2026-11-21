class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp > temperatures[stack[-1]]:
                day = stack.pop()
                results[day] = (i-day)
            stack.append(i)
        return results 
    


    
         







   