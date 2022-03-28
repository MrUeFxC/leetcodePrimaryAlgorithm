import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dict1 = collections.Counter(s)
        dict2 = collections.Counter(t)
        if dict1 == dict2:
            return True
        else:
            return False


str1 = "anagram"
str2 = "sagaram"


s = Solution()
result = s.isAnagram(str1, str2)
print(result)