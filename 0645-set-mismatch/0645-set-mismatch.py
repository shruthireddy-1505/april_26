class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = set(nums)
        d = {}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i] = 1
        for k,v in d.items():
            if v>1:
                temp = k-1
                tempin = k+1
                while temp>0:
                    if temp not in n:
                        return [k,temp]
                    temp-=1
                while tempin<=max(n)+1:
                    if tempin not in n:
                        return [k,tempin]
                    tempin += 1
        

        