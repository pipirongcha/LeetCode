class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([1]*(i+1))
            if i > 1:
                for j in range(len(res[i-1])):
                    if j != 0 and j != len(res[i-1]): 
                        res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
        