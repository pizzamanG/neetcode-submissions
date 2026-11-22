class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            canonical = ''.join(sorted(s))
        
            hashmap.setdefault(canonical, []).append(s)
        


        arr = []
        for key in hashmap:
            arr.append(hashmap[key])

        return arr


           


        