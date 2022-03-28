class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)

        ans = ''
        start, end = 0,0
        while end < len(s):
            while end < len(s) and s[start] == s[end]:
                end += 1
            ans += str(end - start) + s[start]
            start = end
        return ans



n = 5
s = Solution()
result = s.countAndSay(n)
print(result)