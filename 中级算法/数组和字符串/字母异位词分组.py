from typing import List
from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        listDic = {}
        for i in range(len(strs)):
            sortedStr = ''.join(sorted(strs[i]))
            if sortedStr in listDic.keys():
                listDic[sortedStr].append(strs[i])
            else:
                listDic[sortedStr] = [strs[i]]
        return list(listDic.values())


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
result = s.groupAnagrams(strs)
print(result)