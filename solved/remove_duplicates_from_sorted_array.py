# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = []
        for i in range(0, len(nums) - 1):
            if nums[i] == nums[i + 1]:
                d.append(nums[i])

        for i in d:
            nums.remove(i)

        return len(nums)