class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        lenStr = len(s)
        for i in range(lenStr//2):
            s[i],s[-i-1] = s[-i-1],s[i]
        return s

str = ["h","e","l","l","o"]
s = Solution()
result = s.reverseString(str)
print(result)