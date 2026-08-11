from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = {}

        for string in strs:
            idx = {k:0 for k in range(26)}
            for s in string:
                idx[ord(s)-97]+=1
            srt = tuple([(k,v) for k,v in idx.items()])
            if srt in tracker:
                tracker[srt].append(string)
            else:
                tracker[srt] = [string]
        return list(tracker.values())

        