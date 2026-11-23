class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        row_bool = any(i==0 for i in [matrix[i][0] for i in range(len(matrix))])

        col_bool = any(i==0 for i in [matrix[0][i] for i in range(len(matrix[0]))])


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        
      #fix rows
        for i in range(1,len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        #fix cols
        for i in range(1,len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range( len(matrix)):
                    matrix[j][i] = 0

        if row_bool:
            for i in range(len(matrix)):
                matrix[i][0] = 0
        if col_bool:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        
        