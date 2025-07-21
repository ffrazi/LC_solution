class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def is_safe(row, col, diagonal, anti_diagonal, cols):
            return (
                col not in cols
                and (row - col) not in diagonal
                and (row + col) not in anti_diagonal
            )

        def backtrack(row, diagonal, anti_diagonal, cols, state):
            if row == n:
                board = []
                for r in state:
                    board.append("".join(r))
                result.append(board)
                return
            for col in range(n):
                if is_safe(row, col, diagonal, anti_diagonal, cols):
                    cols.add(col)
                    diagonal.add(row - col)
                    anti_diagonal.add(row + col)
                    state[row][col] = "Q"
                    backtrack(row + 1, diagonal, anti_diagonal, cols, state)
                    cols.discard(col)
                    diagonal.discard(row - col)
                    anti_diagonal.discard(row + col)
                    state[row][col] = "."

        result = []
        empty_board = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), empty_board)
        return result
