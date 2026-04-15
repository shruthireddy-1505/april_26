class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        d = {}
        for i,v in enumerate(sorted_nums):
            if v not in d:
                d[v] = i
        for i in range(len(nums)):
            nums[i] = d[nums[i]]
        return nums
            
    