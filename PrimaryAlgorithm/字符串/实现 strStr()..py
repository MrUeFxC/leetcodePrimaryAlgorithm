class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(haystack)
        left = 0
        right = len(needle)
        if right == 0:
            return 0
        while right <= n:
            if haystack[left: right] == needle:
                return left
            left += 1
            right += 1
        return -1


haystack = "hello"
needle = "ll"
s = Solution()
result = s.strStr(haystack, needle)
print(result)
