class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        joined = ''.join(e for e in s if e.isalnum()).lower()
        

        return joined[::-1] == joined
        