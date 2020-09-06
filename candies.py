class Solution:
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    def kidsWithCandies(self, candies, extraCandies):
        ans = list()
        most_candies = max(candies)
        for kid in candies:
            if kid + extraCandies >= most_candies:
                ans.append(True)
            else:
                ans.append(False)
        return ans


print(Solution().kidsWithCandies([2, 3, 5, 1, 3], 3))
print(Solution().kidsWithCandies([4, 2, 1, 1, 2], 1))
print(Solution().kidsWithCandies([12, 1, 12], 10))
