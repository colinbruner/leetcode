# https://leetcode.com/problems/shuffle-string/
# COMPLETE
class Solution:
    # def restoreString(self, s: str, indices: List[int]) -> str:
    def restoreString(self, s, indices):
        new_string = ""
        for i in range(len(indices)):
            new_string += s[indices.index(i)]

        return new_string


print(Solution().restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))
print(Solution().restoreString("aiohn", [3, 1, 4, 2, 0]))
