# https://leetcode.com/problems/roman-to-integer
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        num = 0
        prv = None
        for i in reversed(s):
            if prv == None:
                num += romanDict[i]
            elif romanDict[i] >= romanDict[prv]:
                num += romanDict[i]
            else:
                num -= romanDict[i]
            prv = i
        return num

if __name__ == '__main__':
    s = Solution()
    print(s.romanToInt('III'))
    print(s.romanToInt('LVIII'))
    print(s.romanToInt('MCMXCIV'))