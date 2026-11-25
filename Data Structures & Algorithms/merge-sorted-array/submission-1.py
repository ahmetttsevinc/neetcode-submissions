class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1_fr = m+n-1
        pointer1_r = m-1
        pointer2_r = n-1

        while pointer2_r >= 0 and pointer1_r >= 0:
            num1r = nums1[pointer1_r]
            num2r = nums2[pointer2_r]
            if num1r >= num2r:
                nums1[pointer1_fr] = num1r
                pointer1_r += -1
            else: 
                nums1[pointer1_fr] = num2r
                pointer2_r += -1

            pointer1_fr += -1

        while pointer2_r >= 0:
            nums1[pointer1_fr] = nums2[pointer2_r]
            pointer2_r += -1
            pointer1_fr += -1