class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def dfs(cell,i):
            r, c = cell
            if board[r][c] != word[i]:
                return False

            if (board[r][c] == word[i]) and i == len(word)-1:
                return True

            original = board[r][c]
            board[r][c]  =  '#'
            moves =  [(r+1, c),(r-1,c), (r,c+1),(r,c-1)]

            for move in moves:
                r_new, c_new = move
                if 0 <= r_new < len(board) and  0 <= c_new < len(board[0]):
                    if board[r_new][c_new] != '#':
                        res = dfs(move, i+1)
                        if res == True:
                            return True
                
            board[r][c] = original
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != word[0]:
                    continue
                res = dfs((i,j),0)
                if res == True:
                  

                    return True
        return False

            

        