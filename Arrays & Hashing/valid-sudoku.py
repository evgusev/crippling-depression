from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(len(board)):
            row = set()
            for c in range(len(board[r])):
                if (board[r][c] == '.'):
                    continue
                if (board[r][c] in row) or board[r][c] in cols[c] or board[r][c] in squares[(r // 3, c //3 )]:
                    return False
                
                row.add(board[r][c])
                cols[c].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c //3 )].update(board[r][c])

        return True


s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
