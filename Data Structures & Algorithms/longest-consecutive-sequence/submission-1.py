class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        main_list= []
        backup_list=[]
        nums.sort()
        for i,val in enumerate(nums):
            if i == 0:
                main_list.append(val)
                continue

            if nums and val == nums[i-1]:
                continue
            
            if val == main_list[-1]+1:
                main_list.append(val) 
            elif backup_list and val == backup_list[-1]+1: 
                backup_list.append(val)
            else:
                backup_list = [val]
                
            if len(backup_list)> len(main_list):
                main_list = backup_list
                backup_list = [] 

        return len(main_list)

