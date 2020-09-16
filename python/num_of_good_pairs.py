# https://leetcode.com/problems/number-of-good-pairs/
# COMPLETE


class Solution:
    # def numIdenticalPairs(self, nums: List[int]) -> int:
    def numIdenticalPairs(self, nums):
        ans = 0
        for i, x in enumerate(nums):
            ans += nums[i + 1 :].count(x)

        return ans


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(Solution().numIdenticalPairs([1, 1, 1, 1]))
print(Solution().numIdenticalPairs([1, 2, 3]))
