class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # {1:1 , 2:2, 3:3} , {7:2}

        for num in nums:
            count[num] = count.get(num,0) + 1
        
        return sorted(count, key=count.get, reverse=True)[:k]