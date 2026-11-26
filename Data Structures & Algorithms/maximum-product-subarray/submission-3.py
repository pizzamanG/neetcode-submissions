class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        cur_max = nums[0]
        cur_min = nums[0]

        for i in range(1,len(nums)):
            x = nums[i]

            temp_max = x * cur_max
            temp_min = x * cur_min

            cur_max = max(x, temp_max, temp_min)
            cur_min = min(x, temp_max, temp_min)

            best = max(best, cur_max)
        
        return best





           
            





    

        