# https://leetcode.com/problems/sort-an-array/

class Solution:
    def sortArray(self, nums: List[int]):
        min_orig = min(nums)
        min_ = abs(min_orig) if min_orig < 0 else 0
        max_ = max(nums)
        c = min_ + max_ + 1
        out = [0] * c
        for val in nums:
            out[val] += 1
        # print(out, min_orig)
        res = []
        # print(out[-min_:], out[:-min_])
        for i, v in zip(range(-min_, max_+1), out[-min_:] + out[:-min_]):
            if v != 0:
                res = res + [i] * v

        return res


# def countSort(arr):

#     # The output character array that will have sorted arr
#     output = [0 for i in range(256)]

#     # Create a count array to store count of individual
#     # characters and initialize count array as 0
#     count = [0 for i in range(256)]

#     # For storing the resulting answer since the
#     # string is immutable
#     ans = ["" for _ in arr]

#     # Store count of each character
#     for i in arr:
#         count[ord(i)] += 1

#     # Change count[i] so that count[i] now contains actual
#     # position of this character in output array
#     for i in range(256):
#         count[i] += count[i-1]

#     # Build the output character array
#     for i in range(len(arr)):
#         output[count[ord(arr[i])]-1] = arr[i]
#         count[ord(arr[i])] -= 1

#     # Copy the output array to arr, so that arr now
#     # contains sorted characters
#     for i in range(len(arr)):
#         ans[i] = output[i]
#     return ans
