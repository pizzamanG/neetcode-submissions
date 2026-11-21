class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        # frequency maps for s1 and current window in s2
        freq_s1 = {}
        freq_win = {}
        for ch in s1:
            freq_s1[ch] = freq_s1.get(ch, 0) + 1
        
        l = 0
        for r in range(len(s2)):
            # add current char to window
            freq_win[s2[r]] = freq_win.get(s2[r], 0) + 1
            
            # shrink window if it’s longer than s1
            if r - l + 1 > len(s1):
                left_char = s2[l]
                freq_win[left_char] -= 1
                if freq_win[left_char] == 0:
                    del freq_win[left_char]
                l += 1

            # check equality when window size matches
            if r - l + 1 == len(s1) and freq_win == freq_s1:
                return True
        
        return False
