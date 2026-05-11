class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0 
        dp = [1] * len(nums)
        new_lst = sorted(set(nums))
        print(new_lst)
        for i in range(1, len(new_lst)):
            if new_lst[i] == new_lst[i - 1] + 1:
                dp[i] = dp[i - 1] + 1
        return max(dp)