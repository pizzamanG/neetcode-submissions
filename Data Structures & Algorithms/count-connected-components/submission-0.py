





from collections import deque 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        adj = {}
        from collections import defaultdict
        adj = defaultdict(set)
        for i in edges:
            source, target = i
            adj[source].add(target)
            adj[target].add(source)

        visited = set()
        components = 0

        def bfs(edges, node, visited):
            queue= deque([node])
            while queue:
                n = queue.popleft()
                if n not in visited:
                    visited.add(n)

                    for nei in list(adj[n]):
                        queue.append(nei)
                
        
        for edge in range(n):
            if edge not in visited:
                components +=1
                bfs(edges,edge, visited)

        return components



        