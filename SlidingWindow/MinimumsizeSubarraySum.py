class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        summ=0
        length=float('inf')
        if len(nums)==1:
            if nums[l]>=target:
                return 1
            else:
                return 0
        r=l
        while r<len(nums):
            summ+=nums[r]
            while summ>=target:
                summ-=nums[l]
                length=min(r-l+1,length)
                l+=1
        
            r+=1
            

        if length==float('inf'):
            return 0
        return length
