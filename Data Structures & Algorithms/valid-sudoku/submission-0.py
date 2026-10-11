class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # box 0 -- row 0 to 2, col 0 to 2
        # box 1 -- row 3 to 5, ...
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxes = [set() for i in range(9)]

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '.':
                    col += 1
                    continue
                if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in boxes[(row // 3) * 3 + (col // 3)]:
                    return False
                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxes[(row // 3) * 3 + (col // 3)].add(board[row][col])
                col += 1
            row += 1
        
        return True
                