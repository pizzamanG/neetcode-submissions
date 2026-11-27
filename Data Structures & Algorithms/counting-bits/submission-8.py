class Solution:
    def countBits(self, n: int) -> List[int]:
       
        digits = [0]
        power = 0


        for i in range(1,n+1):

            while 2**power <= i:
                power +=1
            power -=1
         
      
            remainder = i
            subtotal = 0

        
            remainder -= 2**power
            subtotal +=1
            subtotal += digits[remainder]

              
            digits.append(subtotal)
        return digits
        

       
        