class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            check=set()
            for j in range(len(board[i])):
                if board[i][j]=='.':
                    continue
                if board[i][j] in check :
                    return False
                check.add(board[i][j])
        for i in range(len(board)):
            check=set()
            for j in range(len(board)):
                if board[j][i] in check:
                    return False
                if board[j][i]=='.':
                    continue
                check.add(board[j][i])
        for i in range(0,len(board),3):
            for j in range(0,len(board),3):
                check=set()
                for k in range(3):
                    for l in range(3):
                        value=board[i+k][j+l]
                        if value=='.':
                            continue
                        if value  in check:
                            return False
                        check.add(value)
        return True
                 