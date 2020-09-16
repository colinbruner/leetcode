# https://leetcode.com/explore/challenge/card/september-leetcoding-challenge/554/week-1-september-1st-september-7th/3447/
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)):
            substring = s[0:i]
            while len(substring) <= len(s):
                substring += s[0:i]
                if substring == s:
                    return True

        return False


print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("aba"))
