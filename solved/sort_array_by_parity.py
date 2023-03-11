# https://leetcode.com/problems/sort-array-by-parity/

class Solution:
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:

        a = [x for x in nums if x % 2 == 0]
        b = [x for x in nums if x % 2]

        return a + b


class Solution:
    def sortArrayByParity1(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] % 2 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

            elif nums[l] % 2 == 0:
                l += 1

            elif nums[r] % 2:
                r -= 1

        return nums
