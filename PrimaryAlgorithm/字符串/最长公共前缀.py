class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        headStr = ''
        flag = True
        loc = 0
        while flag == True:
            for j in range(len(strs)):
                if loc > len(strs[j]) - 1:
                    flag = False
            if flag == False:
                break
            strCurrent = strs[0][loc]
            for i in range(1, len(strs)):
                if strCurrent != strs[i][loc]:
                    flag = False
            if flag == True:
                headStr += strCurrent
            loc += 1
        return headStr




strs = ["fl","flow","floight"]
s = Solution()
result = s.longestCommonPrefix(strs)
print(result)