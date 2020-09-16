from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        [ans.insert(index[i], nums[i]) for i in range(len(index))]
        return ans


print(Solution().createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
