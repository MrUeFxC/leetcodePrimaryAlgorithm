class Solution:
    # def longestPalindrome(self, s) -> str:
        # maxSTr = ''
        # n = len(s)
        # if n == 1:
        #     return s[0]
        # for i in range(n):
        #     startStr = s[i]
        #     for j in range(n-1, i, -1):
        #         isPalindrome = True
        #         if startStr == s[j]:
        #             start = i
        #             end = j
        #             while start < end:
        #                 if s[start] != s[end]:
        #                     isPalindrome = False
        #                     break
        #                 start += 1
        #                 end -= 1
        #             if isPalindrome ==True and j-i+1 >len(maxSTr):
        #                 maxSTr = s[i:j+1]
        # if len(maxSTr)==0:
        #     return s[0]
        # return maxSTr

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]


str = "aba"
s = Solution()
result = s.longestPalindrome(str)
print(result)