class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        l = 0
        r = 0
        best = 0
        while r < len(s):
            
            if s[r] not in hashmap:
                hashmap[s[r]] =1
            else:
                hashmap[s[r]] +=1


            majority = max(hashmap.values())
            #how many characters in the window total
            win_length = (r-l) + 1
            
            ceiling = (win_length- majority)


            if ceiling <= k:
                best = max(best,  win_length)

            while ceiling > k:
                hashmap[s[l]] -=1
                l +=1
                majority = max(hashmap.values())
                win_length = (r-l) + 1
            
                ceiling = (win_length- majority)
            r +=1
        return best


          


            
          


        
    