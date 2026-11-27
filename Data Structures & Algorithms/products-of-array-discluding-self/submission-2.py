class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        start = 1
        left = []
        for i in nums:
            start *= i
            left.append(start)

        right = []
        start = 1
        for i in nums[::-1]:
            start *=i
            right.append(start)

        output = []

        
        for i in range(len(nums)):
            if  i == 0:
                left_subtotal = 1
            else:
                left_subtotal = left[i-1]
            
            if i == len(nums) -1:
                right_subtotal = 1
            else:
                right_subtotal = right[len(nums) - i - 2]
            
            output.append(left_subtotal * right_subtotal)

        return output
  

       
            




        