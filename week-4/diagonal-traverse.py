class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        my_dict = defaultdict(list)
        res = []

        for i in range(rows):
            for j in range(cols):
                my_dict[i + j].append(mat[i][j])

        for k in range(rows + cols - 1):
            if k % 2 == 0:
                res.extend(my_dict[k][::-1])
            else:
                res.extend(my_dict[k])
        return res