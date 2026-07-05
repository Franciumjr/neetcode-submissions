class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        hashmap = {}
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else: 
                hashmap[num] += 1
        
        while k:
            res.append(max(hashmap, key=hashmap.get))
            hashmap.pop(max(hashmap, key=hashmap.get))
            k -= 1
        
        return res
