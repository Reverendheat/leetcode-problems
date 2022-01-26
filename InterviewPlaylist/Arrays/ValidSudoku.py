from typing import List
from collections import defaultdict

"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1s-9 without repetition.
"""

board = [
    [".", ".", ".", ".", "5", ".", ".", "1", "."],
    [".", "4", ".", "3", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "3", ".", ".", "1"],
    ["8", ".", ".", ".", ".", ".", ".", "2", "."],
    [".", ".", "2", ".", "7", ".", ".", ".", "."],
    [".", "1", "5", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", ".", ".", "2", ".", ".", "."],
    [".", "2", ".", "9", ".", ".", ".", ".", "."],
    [".", ".", "4", ".", ".", ".", ".", ".", "."],
]


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # # Could use array here too.
        # cols = defaultdict(set)
        # rows = defaultdict(set)
        # squares = defaultdict(set)

        # for r in range(9):
        #     for c in range(9):
        #         print(squares)
        #         if board[r][c] == ".":
        #             continue
        #         if (
        #             board[r][c] in rows[r]
        #             or board[r][c] in cols[c]
        #             or board[r][c] in squares[(r // 3, c // 3)]
        #         ):
        #             return False
        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r // 3, c // 3)].add(board[r][c])
        # return True

        # MY ATTEMPT, couldn't get the 3x3 portion (isInCube) to work...
        for i in range(len(board)):
            inRow = self.isInRow(board, i)
            inColumn = self.isInColumn(board, i)
            inCube = self.isInCube(board, i)
            if inRow and inColumn and inCube:
                continue
            else:
                return False
        return True

    def isInRow(self, board, row):
        r = []
        for i in range(len(board[row])):
            if board[row][i] == ".":
                continue
            if not isinstance(int(board[row][i]), int) or int(board[row][i]) >= 10:
                return False
            if board[row][i] in r:
                return False
            else:
                r.append(board[row][i])
        return True

    def isInColumn(self, board, col):
        c = []
        for i in range(len(board)):
            if board[i][col] == ".":
                continue
            elif board[i][col] in c:
                return False
            else:
                c.append(board[i][col])
        return True

    def isInCube(self, board, r):
        n = []
        for c in range(9):
            if board[r][c] == ".":
                continue
            if board[r][c] in n:
                return False
            n.append(board[r][c])
        return True


s = Solution()
print(s.isValidSudoku(board))
