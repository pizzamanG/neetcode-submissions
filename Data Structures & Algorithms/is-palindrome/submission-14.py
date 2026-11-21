


class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_a = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
     
        for l in range((len(str_a)//2)):
            r = len(str_a)-1-l
            print(l,r , len(str_a), str_a)
          
            if str_a[l]!=str_a[r]:
               
                return False
            print(l)
        return True 
        