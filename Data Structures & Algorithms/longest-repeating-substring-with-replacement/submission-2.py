class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        end = 0
        maxi = 0
        count = 0
        for start in range(len(s)):
            freq[s[start]] = freq.get(s[start], 0) + 1
            maxi = max(maxi, freq[s[start]])
            size = start - end + 1
            if size - maxi > k:
                freq[s[end]] -= 1
                end += 1
            count = max(count, start - end + 1)
        return count


            






                