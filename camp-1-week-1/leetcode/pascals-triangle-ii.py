class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #bestcase-1&2
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1,1]
        else:
            prev_row = self.getRow( rowIndex-1 )
            row = [1]
            for i in range(1,rowIndex):
                now = prev_row[i-1] + prev_row[i]
                row.append( now )

            row.append(1)
            return row
