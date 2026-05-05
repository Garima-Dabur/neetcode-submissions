class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        last = len(numbers) - 1
        while first < last:
            t = numbers[first] + numbers[last]
            if t < target:
                first += 1
            elif t > target:
                last -= 1
            else:
                return [first + 1, last + 1]

        