class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()
        MAX_INT, MIN_INT = 2**31-1, -2**31
        flag = 1
        num = 0
        i = 0
        lenStr = len(s)
        if lenStr == 0:
            return 0
        if s[0] == '-' or s[0] == '+' and lenStr >= 2:
            if s[0] == '-':
                flag = -1
            i = 1
        elif s[0].isnumeric() == False or s[i].isnumeric() == False:
            return 0
        for str in s[i:]:
            if str.isnumeric():
                num = num*10 + int(str)
            else:
                break

        num *= flag
        if num > MAX_INT:
            return MAX_INT
        elif num < MIN_INT:
            return MIN_INT
        return num

str = "+"
s = Solution()
result = s.myAtoi(str)
print(result)