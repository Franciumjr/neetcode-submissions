class Solution:
    def isValid(self, s: str) -> bool:
        # hashmap matching parantheses
        stk = []
        closetoOpen = {
            "}": "{",
            "]": "[",
            ")": "(",
        }
        # iterate through each char in s
        for char in s:
            if char in closetoOpen:
                # if there is something in stk, and the last char in
                # stk is an opening bracket
                if stk and stk[-1] == closetoOpen[char]:
                    stk.pop()
                else:
                    return False
        #if the char is closing, return False
            else:
                stk.append(char)
        # if the char is an opening, continue 
        return True if not stk else False

