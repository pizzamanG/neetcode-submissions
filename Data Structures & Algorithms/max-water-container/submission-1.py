class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) -1 
        best = 0

        def get_vol(l,r):
            x = (r -l)
            y = min(heights[l], heights[r])
            return x * y

        while l < r:
            area = get_vol(l, r)
            best = max(best, area)
            if heights[l] <= heights[r]:
                l +=1
                
            elif heights[r] <= heights[l]:
                r -=1
               
        
        return best 



        