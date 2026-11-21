



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        al = set(nums)


        best = 0

       
 
        for i in al:
            if (i-1)  in al:
                continue
            count = 0
            current = i 
            while current in al:
                current +=1 
                count +=1

           
            best = max(best,count)
                
        
        return best
                



        
               






       





    

      


      