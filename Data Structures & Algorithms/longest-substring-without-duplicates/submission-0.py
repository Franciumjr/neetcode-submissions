class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, r = 0, 0
        longest_streak = 0

        while (r < len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            longest_streak = max(longest_streak, r -l + 1)
            r += 1


        
        return longest_streak
