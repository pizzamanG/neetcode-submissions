class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
       
        l = 0
        r = 0
        
        while r < len(s):
            if s[r] not in seen:
                best = max(r-l+1, best)
                seen.add(s[r])
            
              
            elif s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l +=1
                seen.add(s[r])
                best = max(r-l+1, best)
                     
              
            r +=1
      
        return best 
                    
                

                
        