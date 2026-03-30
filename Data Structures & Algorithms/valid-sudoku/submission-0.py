class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = [[set() for _ in range(9)] for _ in range(3)]

        for i in range(len(board)):
            for j in range(len(board[i])):
                item = board[i][j]

                if item == ".": 
                    continue

                k = (i//3)*3 + j//3

                if item in rows[i] or item in cols[j] or item in boxes[k]:
                    return False

                rows[i].add(item)
                cols[j].add(item)
                boxes[k].add(item)
            
        return True;