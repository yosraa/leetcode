# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

class Solution:
    def addDigits(self, num: int) -> int:
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            res = 0
            while num:
                res += num%10
                num = num//10
                
            num = res
        return num

      
class Solution:
    def addDigits(self, num: int) -> int:
        return num%9 if num%9!=0 or num==0 else 9
