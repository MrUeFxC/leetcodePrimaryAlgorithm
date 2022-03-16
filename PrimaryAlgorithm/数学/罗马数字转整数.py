class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        dic = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        lenStr = len(s)
        i = 0
        while i < lenStr:
            if i < lenStr-1 and (s[i] == 'I' or s[i] == 'X' or s[i] == 'C'):
                if s[i] == 'I' and s[i+1] == 'V':
                    num += 4
                    i += 1
                elif s[i] == 'I' and s[i+1] == 'X':
                    num += 9
                    i += 1
                elif s[i] == 'X' and s[i+1] == 'L':
                    num += 40
                    i += 1
                elif s[i] == 'X' and s[i+1] == 'C':
                    num += 90
                    i += 1
                elif s[i] == 'C' and s[i+1] == 'D':
                    num += 400
                    i += 1
                elif s[i] == 'C' and s[i+1] == 'M':
                    num += 900
                    i += 1
                else:
                    num += dic[s[i]]
                i += 1
            else:
                num += dic[s[i]]
                i += 1
        return num



str = "MDLXX"
s = Solution()
result = s.romanToInt(str)
print(result)