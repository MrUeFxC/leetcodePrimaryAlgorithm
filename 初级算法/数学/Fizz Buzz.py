from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        listFizzBuzz = []
        for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0:
                listFizzBuzz.append('FizzBuzz')
            elif i % 3 == 0:
                listFizzBuzz.append('Fizz')
            elif i % 5 == 0:
                listFizzBuzz.append('Buzz')
            else:
                listFizzBuzz.append(str(i))
        return listFizzBuzz

n = 15
s = Solution()
result = s.fizzBuzz(n)
print(result)