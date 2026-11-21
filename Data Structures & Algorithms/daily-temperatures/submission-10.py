class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        current_max = 0
        t_stack = [0]
        results = [0] * len(temperatures)
        for i  in range(1, len(temperatures)):
            t = temperatures[i]
           
            while t_stack and t > temperatures[t_stack[-1]]:
                day = t_stack.pop()
                results[day] = (i - day)

      
            t_stack.append(i)

        return results 



   