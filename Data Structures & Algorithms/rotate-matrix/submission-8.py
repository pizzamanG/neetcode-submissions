class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        for c in range(0,len(matrix[0])):
             
            for r in range(c, -1,-1):
                if c != r:
                    matrix[c][r], matrix[r][c] = matrix[r][c], matrix[c][r]
        



        for c in range(len(matrix[0]) //2):
            for r in range(0, len(matrix)):
                matrix[r][c], matrix[r][len(matrix[0])-c-1]  = matrix[r][len(matrix[0])-c-1],matrix[r][c]

        return None

        