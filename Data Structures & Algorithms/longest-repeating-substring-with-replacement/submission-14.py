class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import Counter

        l = 0
        best = 0
        win = Counter()
        for r in range(len(s)):
            win[s[r]] +=1

            while (r-l+1) - win.most_common(1)[0][1] > k:
                win[s[l]] -=1
                l += 1
              

            best = max(best, r-l+1)

        return best
            


        




        







      



        