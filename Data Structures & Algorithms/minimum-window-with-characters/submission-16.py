class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        from collections import Counter
        window = {}
        target = Counter(t)
        need = len(target)
        have = 0
        res = [0,1e9]

        l, r = 0,0


        while r <len(s):
            if s[r] in target:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == target[s[r]]:
                    have +=1
                
            while need == have:
                
                   
                if (r - l) < (res[1] - res[0]):
                     res = [l, r]

                
                if s[l] in window:
                    window[s[l]] -=1
                if s[l] in target and window[s[l]] < target[s[l]]:
                    have -=1
                l+=1

                
            r +=1
        if res[1] == 1e9:
            return ""

        return s[res[0]: res[1]+1]


