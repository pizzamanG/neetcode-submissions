class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eating_time(k, pile):
            return (pile + k -1) // k
        
        l = 1
        r = max(piles)

        def search(l, r, h, best):
            if l > r:
                return best
            
            median = l + (r-l)//2
            time = sum([eating_time(median, i) for i in piles])
            if time <=h:
                best = min(best, median)
                return search(l, median-1, h, best)
            return search(median+1, r, h , best)

        best = search(l, r, h, r)
        return best

    

        


    