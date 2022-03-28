class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '}':'{',
            ']':'[',
            ')':'('
        }
        stack = []
        isVaild = True
        for i in range(len(s)):
            if s[i] in parentheses.keys() and len(stack) != 0:
                if stack.pop() != parentheses[s[i]]:
                    isVaild = False
                    break
            else:
                stack.append(s[i])
        return isVaild and len(stack) == 0

str = "]"
s = Solution()
result = s.isValid(str)
print(result)