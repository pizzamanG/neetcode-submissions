class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        


        def dfs(node,ocean):
            if node in ocean:
                return None
            ocean.add(node)
      
            r, c = node
            level = heights[r][c]
            dirs = [(r+1,c),(r-1,c), (r,c-1),(r,c+1)]

            for new_node in dirs:
                r_new = new_node[0]
                col_new = new_node[1]

                if 0 <= r_new < len(heights) and 0 <= col_new <len(heights[0]):
                   
                    new_level = heights[r_new][col_new]
                    if new_level >= level:
                        dfs(new_node,ocean)
        

        for i in range(len(heights)):
            dfs((i,0),pacific)
            dfs(  (i, len(heights[0]) -1)  ,atlantic)
        
        for i in range(len(heights[0])):
            dfs((0,i),pacific)
            dfs((len(heights)-1,i),atlantic)
        
        return sorted(list(pacific & atlantic))
        




        