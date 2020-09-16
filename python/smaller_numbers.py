class Solution:
    # def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
    def smallerNumbersThanCurrent(self, nums):
        out = []
        for i in range(len(nums)):
            smaller = 0
            for number in nums:
                if nums[i] > number:
                    smaller += 1
            out.append(smaller)

        return out


print(Solution().smallerNumbersThanCurrent([8, 1, 2, 2, 3]))
