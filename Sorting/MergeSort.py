class Solution:
    def __init__(self):
        pass
    def mergesort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            Larr=arr[:mid]
            Rarr=arr[mid:]
            self.mergesort(Larr)
            self.mergesort(Rarr)

            i=j=k=0
     
            while i<len(Larr) and j<len(Rarr):
                if Larr[i]<Rarr[j]:
                    arr[k]=Larr[i]
                    i+=1
                   
                else:
                    arr[k]=Rarr[j]
                    j+=1
                k+=1
            while i<len(Larr):
                arr[k]=Larr[i]
                i+=1
                k+=1
            while j<len(Rarr):
                arr[k]=Rarr[j]
                j+=1
                k+=1
      
        
        

       
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergesort(nums)
        return nums
        
