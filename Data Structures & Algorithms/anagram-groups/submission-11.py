class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        pairing = defaultdict(list)
        for st in strs:
            arr = [0] * 26
            for c in st:
                arr[ord(c) - ord('a')] += 1;
            pairing[tuple(arr)].append(st)
        return list(pairing.values())

        