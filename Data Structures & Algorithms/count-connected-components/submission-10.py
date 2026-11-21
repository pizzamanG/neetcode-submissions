





from collections import deque 
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connections = 0 
        from collections import defaultdict
        adj = defaultdict(set)

        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)
        visited = set()

        def bfs(start):
            queue = deque([start])

            while queue:
                node = queue.popleft()

                for nei in adj[node]:
                    if nei not in visited:
                        visited.add(nei)
                        queue.append(nei)

        for i in range(n):
            if i not in visited:
                connections +=1
                bfs(i)
        return connections