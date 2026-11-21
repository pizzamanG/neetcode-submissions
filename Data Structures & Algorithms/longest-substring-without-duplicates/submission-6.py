class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
       
        l = 0
        r = 0
        
        while r <len(s):
            if s[r] not in seen:
                seen.add(s[r])
                best = max(best, r-l+1)

            elif s[r] in seen:
                while  s[r] in seen:
                    seen.remove(s[l])
                    l +=1
                seen.add(s[r])
                best = max(best, r-l+1)
            r +=1

        return best

                    
                

                
        