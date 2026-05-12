class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        new_lst = sorted(nums)
        final = []

        for i in range(len(nums)):
            if i > 0 and new_lst[i] == new_lst[i - 1]:
                    continue
            start = i + 1
            end = len(new_lst) - 1

            while start < end:
                t = new_lst[i] + new_lst[start] + new_lst[end]
                if t < 0 :
                    start += 1
                elif t > 0:
                    end -= 1
                else:
                    final.append([new_lst[i], new_lst[start], new_lst[end]])
                    start += 1
                    end -= 1
                    while start < end and new_lst[start] == new_lst[start - 1]:
                        start += 1
        return final 
