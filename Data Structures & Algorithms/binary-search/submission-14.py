class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l,r ):
            if l > r :
                return -1
            median = l + (r-l) //2
            if nums[median] == target:
                return median
            elif nums[median] < target:
                return binary_search(median+1, r)
            elif nums[median] > target:
                return binary_search(l, median-1)
        return binary_search(0, len(nums)-1)

     