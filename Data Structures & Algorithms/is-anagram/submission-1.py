class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        tracker = {}

        for letter in s:
            if letter in tracker:
                tracker[letter] += 1
            else:
                tracker[letter] = 1
        
        for letter in t:
            if letter in tracker:
                tracker[letter] -= 1
        
        return all(x == 0 for x in tracker.values())

        