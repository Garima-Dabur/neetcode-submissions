class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxi = 0
        while start < end:
            height = min(heights[start], heights[end])
            temp = (end - start) * height 
            if temp > maxi:
                maxi = temp
            if heights[start] < heights[end]:
                start += 1
            else:
                end -=1 
        return maxi

        