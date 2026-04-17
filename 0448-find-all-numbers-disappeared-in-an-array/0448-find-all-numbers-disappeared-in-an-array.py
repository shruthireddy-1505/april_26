class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [0]*n
        for i in range(len(nums)):
            temp[nums[i]-1] = 1
        ans = []
        for i in range(len(nums)):
            if temp[i]== 0:
                ans.append(i+1)
        return ans

        