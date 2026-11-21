class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        t_stack = []
        results = [0] * len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while t_stack and temperatures[t_stack[-1]] < temp:
                day = t_stack.pop()
                results[day] = i - day
            t_stack.append(i)
        return results


    
         







   