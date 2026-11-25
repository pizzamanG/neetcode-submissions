class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        freqs = {}
        for i in nums:
            dic[i] = dic.get(i,0) +1


        for num, v in dic.items():
            if v not in freqs:
                freqs[v] = []
          
            freqs[v].append(num)


        res = []


        for i in range(len(nums),0, -1):
            if i not in freqs:
                freqs[i] = []
            if freqs[i] != []:
                for num in freqs[i]:
                    res.append(num)
                    if len(res) == k:
                        return res

            


        


        

        