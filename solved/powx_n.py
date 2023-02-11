# https://leetcode.com/problems/powx-n/submissions/895852526/

# class Solution:
#     def myPow(self, x: float, n: int) -> float:

#         if n == 0:
#             return 1

#         i = abs(n)
#         r = 1
#         while i > 0:

#             r = r * x if n > 0 else r / x

#             i -= 1
#         return r


class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n == 0:
            return 1

        if n < 0:
            x = 1/x
            n = abs(n)

        if n % 2 == 0:
            return self.myPow(x * x, n // 2)
        return self.myPow(x, n - 1) * x
