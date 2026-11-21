class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def eating_time(k, bananas):
            return (bananas + k -1) // k
        
        piles = sorted(piles)
        r = piles[-1]
        l = 1

  

        def bin_search(l, r, h, best):
            if l > r:
                return best
        
            median = (l + (r-l) // 2)
            time = sum([eating_time(median,i) for i in piles])
            if time <= h:
                best = min(best, median)
                return bin_search(l, median -1, h ,best)
            else:
               return  bin_search(median+1, r, h , best)
        best = bin_search(l,r, h, max(piles))
        return best
                    

     

        


    