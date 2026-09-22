import random
from typing import List
class Solution:
    def partition(self, nums:List[int], left:int, right:int) -> int:
        pivot_idx=random.randint(left,right)
        nums[right],nums[pivot_idx]=nums[pivot_idx],nums[right]

        pivot=nums[right]
        i=left
        for j in range(left,right):
            if nums[j]<pivot:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
        nums[i],nums[right]=nums[right],nums[i]
        return i
    
    def quicksort(self, nums, left, right):
        if left>=right:
            return
        p=self.partition(nums,left,right)
        self.quicksort(nums,left,p-1)
        self.quicksort(nums,p+1,right)

    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums,0,len(nums)-1)
        return nums

