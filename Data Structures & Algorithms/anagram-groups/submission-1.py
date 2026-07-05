from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for text in strs:
            count = [0] * 26 # we keep track of the count for 26 alphabets
                            # count = [0], [0], [0]... [0]
            for char in text:
                count[ord(char) - ord("a")] += 1 # ord() is a function that returns the ascii value

            result[tuple(count)].append(text)
        
        return list(result.values())