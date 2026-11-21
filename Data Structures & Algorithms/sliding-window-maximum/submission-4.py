class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        stack = collections.deque()
        results = []
        l = 0
        r = 0

        while r < len(nums):
 
            while stack and nums[stack[-1]] < nums[r]:
                stack.pop()
            stack.append(r)


            if l > stack[0]:
                stack.popleft()

            if (r+1) >= k:
                results.append(nums[stack[0]])
                l +=1
            r+=1
        return results

            


        