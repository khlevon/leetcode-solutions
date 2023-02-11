# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i, v1 in enumerate(nums):
            for j, v2 in enumerate(nums):
                if v1 + v2 == target:
                    if i == j:
                        continue
                    return i, j
        return -1
