class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        length = len(digits) - 1
        digits[length] = digits[length] + 1
        while (digits[length] == 10 and length > -1):
            digits[length] = 0
            length -= 1
            if length < 0:
                digits.insert(0,1)
            else:
                digits[length] = digits[length] + 1
        return digits

digits = [9,9,9]
s = Solution()
result = s.plusOne(digits)
print(result)