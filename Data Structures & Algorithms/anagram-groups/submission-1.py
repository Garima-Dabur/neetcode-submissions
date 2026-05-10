class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = {}
        for char in strs:
            k = ''.join(sorted(char))

            if k not in freq:
                freq[k] = [char]
            else:
                freq[k].append(char)
        return list(freq.values())
