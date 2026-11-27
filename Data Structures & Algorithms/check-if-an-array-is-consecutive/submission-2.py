class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        n = len(nums)
        return n == len(set(nums)) and max(nums) - min(nums) + 1 == n