class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(board):
            for row in board:
                n=[]
                for i in row:
                    if i.isnumeric(): n.append(i)
                if len(set(n))!=len(n):return False
                print(n)
            return True
        if not validate(board):return False
        if not validate(list(zip(*board))):return False
        tt=[]
        for i in range(0,len(board),3):
            for  j in range(0,len(board),3):
                n=[]
                for t in range(i,i+3):
                    for k in range(j,j+3):
                        if board[t][k].isnumeric():
                            n.append(board[t][k])
                if len(set(n))!=len(n):return False
                tt.append(n)
        return True