class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for x in strs:
    
            canonical = ''.join(sorted(x))
  
            if canonical in hashmap:
                hashmap[canonical].append(x)
            else:
                hashmap[canonical] = [x]
        final = []
        for k, v in hashmap.items():
            answer = list(v)
            final.append(answer)
        return final

        