import string


class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in string.punctuation:
            s = s.replace(i,"")
        s = s.replace(" ","")
        s = s.lower()
        lenStr = len(s)
        for i in range(lenStr//2):
            if s[i] != s[-i-1]:
                return False
        return True

str = "race a car"
s = Solution()
result = s.isPalindrome(str)
print(result)