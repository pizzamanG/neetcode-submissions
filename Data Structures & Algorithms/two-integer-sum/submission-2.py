class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in hash_map:
                return sorted([i, hash_map[complement]])
            hash_map[v] = i 
