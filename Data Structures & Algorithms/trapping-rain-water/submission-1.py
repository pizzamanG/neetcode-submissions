class Solution:
    def trap(self, height: List[int]) -> int:

        prefix_arr = [0] * len(height)
        suffix_arr = [0] * len(height)
        prefix_arr[0] = height[0]
        suffix_arr[-1] = height[-1]

        
        for i in range(1,len(height)):
            curr = height[i]
            prefix_arr[i] = max(curr, prefix_arr[i-1])

        for i in range(len(height)-2, -1, -1):
            
            curr = height[i]
            suffix_arr[i] = max(curr, suffix_arr[i+1])

        amounts = 0

        for i in range(1,len(height)-1):
            pre = prefix_arr[i-1]
            post = suffix_arr[i+1]
            curr_height = height[i]

            boundary = min(pre, post)
            if boundary < curr_height:
                continue
            amounts += boundary - curr_height
          
        return amounts


