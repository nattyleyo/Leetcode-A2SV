class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        matrix = [[0]*len(colSum) for row in range(len(rowSum))]
        min_val = float('inf')
        for i in range( len(rowSum)):
            for j in range( len(colSum)):
                min_val = min( rowSum[i] , colSum[j] )
                if min_val > 0:
                    matrix[i][j] = min_val
                    rowSum[i] -= min_val
                    colSum[j] -= min_val
        return matrix

#[0 7 10]
#[3 8  8]
#[5 0 0]
#[0 0 0]