class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        trackr = {}
        for word in strs:
            if ''.join(sorted(word)) in trackr:
                trackr[''.join(sorted(word))].append(word)
            else:
                trackr[''.join(sorted(word))] = [word]

        return list(trackr.values())
        