class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for i in nums:
            if i not in hashmap:
                hashmap[i] = 1
            else:
                hashmap[i] +=1
        hashmap = sorted(hashmap, key = lambda x : hashmap[x], reverse = True )
        return hashmap[:k]
        
        