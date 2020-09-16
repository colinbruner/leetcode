# https://leetcode.com/problems/decompress-run-length-encoded-list/
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = ""
        while nums:
            f = nums.pop(0)
            i = nums.pop(0)
            ans += f"{i} " * f
        return list(map(int, ans.split()))


print(Solution().decompressRLElist([1, 2, 3, 4]))
