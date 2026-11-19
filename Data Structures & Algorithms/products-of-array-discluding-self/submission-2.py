class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        running_product = 1
        for i in nums:
            left.append(running_product)
            running_product *= i


        right = []
        running_product = 1
        for i in reversed(nums):
            right.append(running_product)
            running_product *= i

        right.reverse()

        result = []
        for i in range(len(nums)):
            result.append(left[i] * right[i])

        return result