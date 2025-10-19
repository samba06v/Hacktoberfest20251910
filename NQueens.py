class Solution:
    def solveNQueens(self, n):
        """
        Backtracking approach to find all valid N-Queen placements.
        """
        res = []
        board = [["."] * n for _ in range(n)]

        def is_valid(row, col):
            for r in range(row):
                if board[r][col] == "Q":
                    return False
                if col - (row - r) >= 0 and board[r][col - (row - r)] == "Q":
                    return False
                if col + (row - r) < n and board[r][col + (row - r)] == "Q":
                    return False
            return True

        def backtrack(row=0):
            if row == n:
                res.append(["".join(r) for r in board])
                return
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        backtrack()
        return res
