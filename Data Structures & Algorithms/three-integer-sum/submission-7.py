class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        results = []
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1

            if i >0 and (nums[i] == nums[i-1]):
                continue


            
       
            while l < r:
                triplet_sum = nums[l] + nums[i] + nums[r]
                if triplet_sum < 0:
                    l +=1
                elif triplet_sum >0:
                    r -=1
                else:
                    results.append(sorted([nums[l], nums[r], nums[i]]))
                    r-=1
                    l+=1

                    while l < r and nums[l] == nums[l-1]:
                        l +=1
                    while l <r and nums[r] == nums[r+1]:
                        r -=1
        return results
            


      




       



