class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        seen = set()
        while i < len(nums):
            if nums[i] not in seen:
                seen.add(nums[i]) ;i += 1
            else: nums.pop(i)

        return len(nums)
