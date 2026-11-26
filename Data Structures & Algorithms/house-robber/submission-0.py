class Solution:
    def rob(self, nums: List[int]) -> int:

        prev2 = 0
        prev1 = 0

        for i in range(len(nums)):

            best = max(nums[i]+ prev2,   prev1)
            prev2 = prev1
            prev1 = best
            
        
        return prev1


        