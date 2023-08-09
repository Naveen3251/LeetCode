class Solution:
    def partition(self,nums,left,right):
        pivot = nums[right]
        j = left-1
        for i in range(left, right):
            if nums[i] < pivot:
                j += 1
                nums[i], nums[j] = nums[j], nums[i]
                
        nums[j+1], nums[right] = nums[right], nums[j+1]
        return j+1
    
    def kthlargest(self,nums,l,r,k):
        index=self.partition(nums,l,r)
        if index==k-1:
            return nums[index]

        elif index>k-1:
            return self.kthlargest(nums,l,index-1,k)
        else:
            return self.kthlargest(nums,index+1,r,k)



    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.kthlargest(nums,0,len(nums)-1,len(nums)-k+1)
