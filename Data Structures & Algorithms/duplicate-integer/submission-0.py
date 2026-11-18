class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        checkList = list()
        for i in nums:
            if i in checkList:
                return True
            else:
                checkList.append(i)
        return False
