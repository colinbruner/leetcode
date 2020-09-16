# https://leetcode.com/problems/shuffle-the-array/submissions/
# COMPLETE


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for a, b in zip(nums[0:n], nums[n:]):
            ans.append(a)
            ans.append(b)

        return ans
