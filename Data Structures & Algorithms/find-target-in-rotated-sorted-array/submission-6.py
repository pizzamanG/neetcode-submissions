class Solution:
    def search(self, nums: List[int], target: int) -> int:

        l = 0
        r  = len(nums) -1

        while l < r:
            mid = l + (r-l) //2
            num = nums[mid]
            if num < nums[r]:
                r = mid
            elif num > nums[r]:
                l = mid + 1

     

        def binary_search(l,r, array, target):
            if l > r:
                return -1
            mid = l + (r-l) //2
            num = array[mid]
            if num == target:
                return mid
            if num < target:
                return binary_search(mid+1, r, array, target)
            
            return binary_search(l, mid-1, array, target)
        
        return max( binary_search(0 ,l-1, nums, target),  binary_search(l, len(nums)-1 , nums, target) )


        


        