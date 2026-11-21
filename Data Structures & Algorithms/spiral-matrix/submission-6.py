class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        visited = set()
        r, c = 0,0
        while len(visited) != len(matrix) * len(matrix[0]):

            while 0<= r < len(matrix) and 0<= c <len(matrix[0]) and (r,c) not in visited:
                arr.append(matrix[r][c])
                visited.add((r,c))
                c +=1
            c-=1
            r+=1
            while 0<= r < len(matrix) and 0<= c <len(matrix[0]) and (r,c) not in visited:
                arr.append(matrix[r][c])
                visited.add((r,c))
                r +=1
            r-=1
            c-=1


            while 0<= r < len(matrix) and 0<= c <len(matrix[0]) and (r,c) not in visited:
                arr.append(matrix[r][c])
                visited.add((r,c))
                c -=1
            c+=1
            r-=1

            while 0<= r < len(matrix) and 0<= c <len(matrix[0]) and (r,c) not in visited:
                arr.append(matrix[r][c])
                visited.add((r,c))
                r -=1
            r+=1
            c+=1


        
        return arr
                
        