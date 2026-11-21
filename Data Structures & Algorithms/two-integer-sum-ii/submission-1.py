class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        r = len(numbers) - 1
        l = 0
        # while (numbers[r] > target) and (r > 0):
        #     r -=1
    
        while l < r:
            complement = target - numbers[r]

            if numbers[l] == complement:
                return [l+1, r+1]
            if numbers[l] > complement:
                l =0
                r -=1
            elif numbers[l] < complement:
                l +=1
            
    
        return [l+1, r+1]
            

            