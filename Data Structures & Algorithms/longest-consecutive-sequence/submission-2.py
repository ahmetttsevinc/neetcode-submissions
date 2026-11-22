class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums) # duplicates are gone

        best_length=0
        
        for n in num_set:
            if n - 1 not in num_set:
                lenght = 1
                while n + lenght in num_set:
                    lenght += 1
                best_length = max(best_length,lenght)
        return best_length

