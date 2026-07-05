class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for index, num in enumerate(nums):
            complement = target- num
            if complement in nums_dict:
                return [nums_dict[complement], index]
            nums_dict[num] = index
        return 
    
