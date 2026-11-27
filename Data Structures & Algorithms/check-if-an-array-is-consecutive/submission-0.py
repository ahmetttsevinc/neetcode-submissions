class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        nums.sort()

        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                continue
            return False
        return True