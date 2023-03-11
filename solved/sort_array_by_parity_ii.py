# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] % 2 and nums[r] % 2 == 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

            elif nums[l] % 2 == 0:
                l += 1

            elif nums[r] % 2:
                r -= 1

        i = 0
        while i < len(nums) // 2:

            if i % 2 != 0:
                nums[-1 - i], nums[i] = nums[i], nums[-1 - i]

            i += 1

        return nums
