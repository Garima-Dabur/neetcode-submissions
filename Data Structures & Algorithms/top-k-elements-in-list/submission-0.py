class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        pair = []
        final = []

        for char in count:
            freq = count[char]
            pair.append((freq, char))
        pair.sort(reverse=True)
        for i in range(k):
            final.append(pair[i][1])

        return final