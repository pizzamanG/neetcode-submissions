
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        def bfs(cell):
            
            q = deque([cell])
            while q:
                tile = q.popleft()
                if tile not in visited:
                    visited.add(tile)
               
                    if grid[tile[0]][tile[1]] == "1":

                        if tile[1] < len(grid[0]) -1:
                            l = (tile[0], tile[1]+1 )
                            q.append(l)
                        if tile[1] > 0:
                            r =  (tile[0] , tile[1]-1 )
                            q.append(r)
                        if tile[0] > 0:
                            u =   (tile[0]-1, tile[1] )
                            q.append(u)
                        if tile[0] < len(grid)-1:
                            d =  (tile[0]+1,tile[1] )
                            print(d)
                            q.append(d)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "0":
                    continue
                else:
                    if (i,j) not in visited:
                        islands +=1
                     
                        
                        bfs( (i,j) )
        return islands



        