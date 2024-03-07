class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited = [ [False for j in range(m)] for i in range(n)]
        res = []
        def backtrack(row,col,idx,visited):
            if idx == len(word):
                return True
            if row < 0 or col < 0 or row >= n or col >= m:
                return False
            elif visited[row][col] or board[row][col] != word[idx]:
                return False

            visited[row][col] = True
           
            
            left = backtrack(row,col-1,idx + 1,visited)
            right = backtrack(row,col+1,idx + 1,visited)
            up = backtrack(row-1,col,idx + 1,visited)
            down = backtrack(row+1,col,idx + 1,visited)
            
            visited[row][col] = False

            return left or right or up or down
             

        for i in range(n): 
            for j in range(m):
                if board[i][j] == word[0]:
                    if backtrack(i,j,0,visited):
                        # print(visited)
                        return True
        return False