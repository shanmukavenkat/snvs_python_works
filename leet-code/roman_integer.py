class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        total = 0
        prev = 0
        for i in s:
            if roman[i] > prev:
                total = total + roman[i] - 2*prev
            else:
                total = total + roman[i]
            prev = roman[i]
        return total