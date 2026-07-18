class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
             return ""

        #count_s, count_t = {}, {}
        window, count_t = {}, {}

        
        #for i in range(len(t)):
            #count_t[t[i]] = 1 + count_t.get(t[i], 0)
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        l = 0
        matches = 0
        goal = len(count_t)

        res, resLen = [-1, -1], float("infinity")
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            #count_s[s[r]] = 1 + count_s.get(s[r], 0)
            if c in count_t and window[c] == count_t[c]:
                matches += 1

            while matches == goal:
                if (r -l + 1 ) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                # pop from the left side of window
                window[s[l]] -= 1
                # if the left side of the longer string is in t, and the s[l]
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    matches -= 1
                l += 1

            


            #if count_s.keys() & count_t.keys():
                #matches += 1
                
            # if its the first term of t, set shrink the window to start
            # from pos r
            
        l, r = res

        return s[l:r+1] if resLen != float("infinity") else ""
        # increase the window length until it founds the 
        
        