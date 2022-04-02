
class Solution:
    def lengthOfLongestSubstring(self, s) -> int:
        # 自己的方法
        maxStr = ''
        curStrs = ''
        for i in range(len(s)):
            curStr = s[i]
            if curStr in curStrs:
                start = curStrs.index(curStr)
                curStrs = curStrs[start+1:] + curStr
                continue
            else:
                curStrs += curStr
                if len(curStrs) > len(maxStr):
                    maxStr = curStrs
        return len(maxStr)

        # 官方方法（滑动窗口）
        # occ = set()
        # n = len(s)
        # rk, ans = -1, 0
        # for i in range(n):
        #     if i != 0:
        #         occ.remove(s[i-1])
        #     while rk + 1 < n and s[rk + 1] not in occ:
        #         occ.add(s[rk + 1])
        #         rk += 1
        #     ans = max(ans, rk - i + 1)
        # return ans







str = 'dvdf'
s = Solution()
result = s.lengthOfLongestSubstring(str)
print(result)