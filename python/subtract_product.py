class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        multi = 1
        for x in str(n):
            multi *= int(x)
        return multi - sum(list(map(int, str(n))))

print(Solution().subtractProductAndSum(234))
