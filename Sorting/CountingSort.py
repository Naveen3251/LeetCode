class Solution:
    def __init__(self):
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
        self.quicksort(nums,0,len(nums)-1)
      
