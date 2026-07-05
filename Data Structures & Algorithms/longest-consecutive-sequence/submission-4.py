class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current_streak = 1
        longest_streak = 1
        if not nums:
            return 0
        nums.sort()
        for i in range(1, len(nums)):
            # skip duplicates
            if nums[i-1] == nums[i]:
                continue
            # we found a streak
            if nums[i-1] + 1 == nums[i]:
                current_streak += 1
            # if the streak broke, we reset the current streak to 0, and set the prev_streak to longest_streak
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1
            
        
        return max(longest_streak, current_streak)
        
        





            
        