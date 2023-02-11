# https://leetcode.com/problems/contains-duplicate/?envType=study-plan&id=data-structure-i

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counts = {}

        for i in nums:
          if not num_counts.get(i, None):
            num_counts[i] = 1
          else:
            return True

        return False
