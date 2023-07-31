class Solution:
    def __init__(self):
        pass
    def countsort(self,nums,exp1):
        count=[0]*10
        output=[0]*len(nums)
        for i in range(len(nums)):
            num=nums[i]//exp1
            count[num%10]+=1

        for i in range(1,10):
            count[i]+=count[i-1]
        
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]//exp1
            output[count[num%10]-1]=nums[i]
            count[num%10]-=1
        for i in range(len(nums)):
            nums[i]=output[i]

    def radixsort(self,nums):
        maxx=max(nums)
        exp=1
        while maxx//exp>=1:
            self.countsort(nums,exp)
            exp*=10
        return nums
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        nums=self.radixsort(nums)
        maximum=0
        for i in range(1,len(nums)):
            maximum=max(maximum,nums[i]-nums[i-1])
        return maximum
        
