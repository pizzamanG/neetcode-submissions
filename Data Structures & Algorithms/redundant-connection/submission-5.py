class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parents = list(range(0, n+1))
        cycles = []

        def find_parent(x):
            if parents[x] != x:
                parents[x] = find_parent(parents[x])
            return parents[x]

        def union(x,y):
            root_x = find_parent(x)
            root_y = find_parent(y)

            if root_x == root_y:
                return True

            parents[root_x] = root_y
            return False 

        
        for i, j in edges:
            if union(i,j):
                cycles.append([i,j])
        
        return cycles[0]