# https://leetcode.com/problems/valid-palindrome/

import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        r_l = re.findall("[^a-zA-Z0-9]", s)

        for item in r_l:
            s = s.replace(item, "")

        s = s.lower()

        l = len(s)
        i = 0
        while i < l // 2:
            if s[i] != s[-i-1]:
                return False

            i += 1

        return True
