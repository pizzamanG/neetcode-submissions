class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = set()
        col = set()
        box = set( )

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                row_key = (i, board[i][j])
                col_key = (j, board[i][j])
                box_key = (i //3,  j // 3, board[i][j])
                print(row_key)

                if row_key in row:
                    return False
                if col_key in col:
                    return False
                if box_key in box:
                    return False
                row.add(row_key)
                col.add(col_key)
                box.add(box_key)
        return True
        