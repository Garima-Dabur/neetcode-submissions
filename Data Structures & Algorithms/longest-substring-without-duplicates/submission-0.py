class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        end = 0
        freq = set()
        for start in range(len(s)):
            while s[start] in freq:
                freq.remove(s[end])
                end += 1
            freq.add(s[start])
            maxi = max(maxi, start - end + 1)
        return maxi 