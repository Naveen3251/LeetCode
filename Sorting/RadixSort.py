class Solution:
    def __init__(self):
        pass

    def countsort(self,nums,exp1):
        length=len(nums)
        count=[0]*10
        output=[0]*length
        for i in range(length):
            num=nums[i]//exp1
            count[num%10]+=1
        for i in range(1,10):
            count[i]+=count[i-1]
        for i in range(length-1,-1,-1):
            num1=nums[i]//exp1
            output[count[num1%10]-1]=nums[i]
            count[num1%10]-=1
        for i in range(length):
            nums[i]=output[i]

    def radixsort(self,nums):
        maxx=max(nums)
        exp=1
        while maxx/exp>=1:
            self.countsort(nums,exp)
            exp*=10
    def sortColors(self, nums: List[int]) -> None:
        self.radixsort(nums)

    '''def __init__(self):
        pass
    def partition(self,nums,low,high):
        i=low-1
        pivot=nums[high]
        for j in range(low,high):
            if nums[j]<pivot:
                i=i+1
                (nums[i],nums[j])=(nums[j],nums[i])
        (nums[i+1],nums[high])=(nums[high],nums[i+1])
        return i+1
    def quicksort(self,nums,low,high):
        if low<high:
            pi=self.partition(nums,low,high)
            self.quicksort(nums,low,pi-1)
            self.quicksort(nums,pi+1,high)
    def sortColors(self, nums: List[int]) -> None:
        self.quicksort(nums,0,len(nums)-1)'''
      
