class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        primary_dict=defaultdict(int)
        secondary_dict=defaultdict(int)
        row=len(mat)
        col=len(mat[0])
        for i in range(row):
            for j in range(col):
                if i-j==0:
                    primary_dict[0]+=mat[i][j]
                if i==j:
                    mat[i][j]=0
                if i+j==col-1:
                    secondary_dict[0]+=mat[i][j]
        tempSum=primary_dict[0]+secondary_dict[0]
        return tempSum

                
        