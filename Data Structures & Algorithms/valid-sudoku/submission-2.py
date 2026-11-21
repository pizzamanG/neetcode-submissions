class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def get_square(row,col):
            row_val = row //3
            col_val = col //3
            return (row_val, col_val)
        #not a board if - row has duplicates, col has duplicates,
        #3*3 region has duplicates
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                square = board[r][c]
                subsquare = get_square(r,c)
                if square == ".":
                    continue
                if (square in rows[r]
                    or square in cols[c]
                    or square in squares[subsquare]):
                        return False
                rows[r].add(square)
                cols[c].add(square)
                squares[subsquare].add(square)
        return True 




 
             
           
                
                
  
            


        