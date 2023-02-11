# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True

        i = 1

        while i <= n:
            i = i << 2

            if i == n:
                return True

        return False
