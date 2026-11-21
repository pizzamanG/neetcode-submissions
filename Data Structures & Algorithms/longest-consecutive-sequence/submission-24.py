class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        longest = 1
        curr = 1


        for i in nums:
            if i-1 in nums:
                curr +=1
                longest = max(curr, longest)
            else:
                
                curr = 1
        return max(longest,curr)
              

        