class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        final = []
        nums.sort()

        #[-4,-1,-1,0,1,2]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]: continue
            first = i + 1
            last = len(nums) - 1
            while first < last:
                remain = nums[i] + nums[first] + nums[last]
                if remain < 0:
                    first += 1
                elif remain > 0:
                    last -= 1
                else:
                    final.append([nums[i], nums[first], nums[last]])
                    first += 1
                    last -= 1
                    while first < last and nums[first] == nums[first-1]: first += 1
        return final