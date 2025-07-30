class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return

        r = len(board)
        c = len(board[0])

        # Step 1: Mark boundary 'O's and their connected 'O's as 'R'
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O' and (i == 0 or i == r - 1 or j == 0 or j == c - 1):
                    self.change(board, i, j)

        # Step 2: Flip unvisited 'O' to 'X' and revert 'R' back to 'O'
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'R':
                    board[i][j] = 'O'

    def change(self, board: list[list[str]], r: int, c: int) -> None:
        if (r < 0 or c < 0 or 
            r >= len(board) or c >= len(board[0]) or 
            board[r][c] != 'O'):
            return

        board[r][c] = 'R'
        self.change(board, r - 1, c)
        self.change(board, r + 1, c)
        self.change(board, r, c - 1)
        self.change(board, r, c + 1)
