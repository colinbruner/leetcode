class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        num = 0
        for stone in S:
            if stone in J:
                num += 1
        return num


print(Solution().numJewelsInStones("aA", "aAAbbbb"))
print(Solution().numJewelsInStones("z", "ZZ"))
