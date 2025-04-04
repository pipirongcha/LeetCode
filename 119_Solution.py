class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        res = [[1] for i in range(rowIndex+1)]
        res[1].append(1)
        for i in range(2,rowIndex+1):
            for j in range(1,len(res[i-1])):
                res[i].append(res[i-1][j-1]+res[i-1][j])
            res[i].append(1)

        return res[rowIndex]


