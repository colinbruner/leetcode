# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len([i for i in nums if len(str(i)) % 2 == 0])


print(Solution().findNumbers([12, 345, 2, 6, 7896]))
