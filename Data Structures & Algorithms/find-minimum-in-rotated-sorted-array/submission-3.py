class Solution:
    def findMin(self, nums: List[int]) -> int:

        def b_search(l,r):
            if (l ==r):
                return l
            
            mid = (l+r) // 2

            if nums[mid] < nums[l]:
                res = b_search(l, mid)
            elif nums[r] < nums[mid+1]:
                res = b_search(mid+1, r)
            
            elif  nums[l] < nums[mid+1]:
                res = b_search(l,mid)
            elif nums[l] > nums[mid+1]:
                res = b_search(mid+1, r)
            return res
              

           
        out = b_search(0,len(nums)-1)

        
        return nums[out]
        

    
     



        