class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0 
        r = len(heights) -1 
        best = 0 

        while (l < r) and r < len(heights) :
            left = heights[l]
            right = heights[r]
            area = (r-l) * min (left,right)

            best = max(area,best)

            if left < right:
                l +=1
            if right <= left:
                r -=1
            


            
        
        return best





        