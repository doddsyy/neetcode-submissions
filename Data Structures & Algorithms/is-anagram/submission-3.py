class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker = {}
        for i in range(len(s)):
            if s[i] in tracker:
                tracker[s[i]] +=1
            else:
                tracker[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] in tracker:
                tracker[t[i]] -=1
            else:
                return False
        
        for k,v in tracker.items():
            if v != 0:
                return False
        return True
