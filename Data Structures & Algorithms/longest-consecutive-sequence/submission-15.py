class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if not nums:
            return 0
        seen = set(nums)
        nums = sorted(list(seen))
        best = 1
        current = 1

        for i in nums:
            if (i-1) not in seen:
                current = 1
            else:
                current +=1
                best = max(current, best)
        best = max(current,best)
      
        return best
            

        