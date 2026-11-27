class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        n = len(nums)

        unique_n = len(set(nums))


        return n == unique_n and max(nums) - min(nums) + 1 == n