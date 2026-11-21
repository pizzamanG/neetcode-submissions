class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(l, r, nums, target):
            if l > r:
                return -1
            m = l + (r-l) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                return binary_search(m+1, r, nums, target)

            return binary_search(l, m-1, nums, target)
        return binary_search(0, len(nums)-1, nums, target)

      