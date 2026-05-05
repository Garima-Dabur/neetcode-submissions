class Solution:
    def maxArea(self, heights: List[int]) -> int:
        first = 0
        last = len(heights) - 1
        maxi = 0
        while first < last:
            mini = min(heights[first], heights[last])
            area = mini * (last - first)
            if maxi < area:
                maxi = area
            if heights[first] <= heights[last]:
                first += 1
            else:
                last -= 1

        return maxi