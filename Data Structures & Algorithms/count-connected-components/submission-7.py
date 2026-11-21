





from collections import deque 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections =0 
        from collections import defaultdict
        adj = defaultdict(set)
        for i, j in edges:
            adj[j].add(i)
            adj[i].add(j)

        visited = set()

        def bfs(start):
            queue = deque([start])
            visited.add(start)

            while queue:
                node = queue.popleft()
                
                   
                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)
        
        for i in range(n):
            if i not in visited:
                bfs(i)
                connections += 1
        return connections




        