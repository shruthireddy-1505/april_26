class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        j=1
        t=0
        ans = []
        while t<len(nums)//2:
            ans.append(nums[j])
            ans.append(nums[i])
            i+=2
            j+=2
            t+=1
        return ans
