class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])
        self.pref=[[0 for i in range(col+1)] for j in range(row+1)]
        for i in range(1,row+1):
            for j in range(1,col+1):
                self.pref[i][j] = self.pref[i-1][j] + self.pref[i][j-1] + matrix[i-1][j-1] - self.pref[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sub_matSum = self.pref[row2+1][col2+1] - self.pref[row2+1][col1] - self.pref[row1][col2+1] + self.pref[row1][col1] 
        return sub_matSum   


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)