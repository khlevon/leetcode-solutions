# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i = 0
        l = len(s)

        r = 0

        while i < l:
            if i != l-1:
                if s[i] == "I":
                    if s[i+1] == "V":
                        r += 4
                        i += 2
                        continue
                    if s[i+1] == "X":
                        r += 9
                        i += 2
                        continue
                if s[i] == "X":
                    if s[i+1] == "L":
                        r += 40
                        i += 2
                        continue
                    if s[i+1] == "C":
                        r += 90
                        i += 2
                        continue
                if s[i] == "C":
                    if s[i+1] == "D":
                        r += 400
                        i += 2
                        continue
                    if s[i+1] == "M":
                        r += 900
                        i += 2
                        continue

            r += romans[s[i]]
            i += 1
        return r


# symbolToIntDict = {"I": 1,
#                    "V": 5,
#                    "X": 10,
#                    "L": 50,
#                    "C": 100,
#                    "D": 500,
#                    "M": 1000}

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         prevValue = symbolToIntDict["M"]
#         totalValue = 0
#         for c in s:
#             currentValue = symbolToIntDict[c]
#             if prevValue < currentValue:
#                 totalValue -= prevValue * 2
#             totalValue += currentValue
#             prevValue = currentValue
#         return totalValue


# "XIV"