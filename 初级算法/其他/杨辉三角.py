class Solution:
    def generate(self, numRows: int):
        list = [[1]]
        for i in range(1,numRows):
            listCur = [1] * (i + 1)
            listLast = list[i - 1]
            for j in range(len(list[i-1])-1):
                listCur[1+j] = listLast[j] + listLast[j+1]
            list.append(listCur)
        return list



numRows = 40
s = Solution()
result = s.generate(numRows)
print(result)