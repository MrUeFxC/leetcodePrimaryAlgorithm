class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        time = len(matrix)%2 + len(matrix)//2
        length = len(matrix)
        for i in range(length//2):
            temp = matrix[length-1-i]
            matrix[length-1-i] = matrix[i]
            matrix[i] = temp

        for i in range(length):
            for j in range(i+1, length):
                if i != j:
                    matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]
s = Solution()
result = s.rotate(matrix)
print(result)