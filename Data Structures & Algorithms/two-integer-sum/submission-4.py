class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i in range(len(nums)):
            digit = nums[i]

            comp = target-digit
            if comp in hashmap:
                return sorted(  [i, hashmap[comp]])
            hashmap[digit] = hashmap.get(digit, i)

        
       

        