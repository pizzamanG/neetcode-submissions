class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) -1
        while l < r:
            mid = l + (r-l) //2
            num = nums[mid]
            if num < nums[r]:
                r = mid
            
            elif num > nums[r]:
                l = mid +1

        return nums[l]

       