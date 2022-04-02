from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = set()
        y = set()
        xLen = len(matrix[0])
        yLen = len(matrix)
        for i in range(yLen):
            for j in range(xLen):
                if matrix[i][j] == 0:
                    y.add(i)
                    x.add(j)
        for i in y:
            matrix[i] = [0]*xLen
        for j in x:
            for i in range(yLen):
                matrix[i][j] = 0
        return matrix

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s = Solution()
result = s.setZeroes(matrix)
print(result)