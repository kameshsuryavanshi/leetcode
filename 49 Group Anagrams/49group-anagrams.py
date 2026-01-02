from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for s in strs:
            count =[0]* 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())

        # anagrams = defaultdict(list)
        # [anagrams[tuple(sorted(s))].append(s) for s in strs]
        # return list(anagrams.values())



