from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trackr = {}
        for word in strs:
            if tuple(sorted(Counter(word).items())) in trackr:
                trackr[tuple(sorted(Counter(word).items()))].append(word)
            else:
                trackr[tuple(sorted(Counter(word).items()))] = [word]

        return list(trackr.values())
        