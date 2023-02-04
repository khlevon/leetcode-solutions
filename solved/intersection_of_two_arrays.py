# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = len(nums1)
        out = {}
        res = {}
        for i, val in enumerate(nums1 + nums2):
            if i < n1:
                if not out.get(val, None):
                    out[val] = 1

            
            else:
              if out.get(val, None):
                res[val] = 1

        return res.keys()