class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r,c=len(matrix),len(matrix[0])
        left=0
        right=r*c-1
        print(right)
        while left<=right:
            mid=left+(right-left)//2
            element=matrix[mid//c][mid%c]
            if element==target:
                return True
            elif element<target:
                left=mid+1
            else:
                right=mid-1

       
        return False
