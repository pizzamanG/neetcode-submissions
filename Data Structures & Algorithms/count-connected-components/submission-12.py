class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = [] 

        for pair in edges:
            a,b = pair


            adj.get(a,[]).append(b)
            adj.get(b,[]).append(a)
        visited = set()
        connected = 0 

        for node in adj:
            if node not in visited:
                connected +=1
                q = [node]

                while q:
                    n = q.pop()
                    if n not in visited:
                        visited.add(n)
                        for nei in adj[n]:
                            q.append(nei)
        return connected








            

        